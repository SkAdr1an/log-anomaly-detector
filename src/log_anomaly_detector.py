# src/log_anomaly_detector.py
from dataclasses import dataclass
from typing import Optional
import argparse
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.pipeline import Pipeline


@dataclass
class AnomalyResult:
    data: pd.DataFrame
    model: IsolationForest


def build_pipeline(random_state: int = 42) -> Pipeline:
    # Colunas do gerador: timestamp, user, event_type, ip
    cat_cols = ["event_type", "user", "ip"]
    num_cols: list[str] = []  # adicione features numéricas aqui depois, se quiser

    pre = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
            ("num", StandardScaler(), num_cols),
        ]
    )

    iso = IsolationForest(
        n_estimators=200,
        contamination="auto",
        random_state=random_state,
        n_jobs=-1,
    )

    return Pipeline([("pre", pre), ("model", iso)])


def detect_anomalies(df: pd.DataFrame, contamination: float = 0.02, random_state: int = 42) -> AnomalyResult:
    pipe = build_pipeline(random_state=random_state)
    pipe.named_steps["model"].set_params(contamination=contamination)

    # garante datetime
    if not pd.api.types.is_datetime64_any_dtype(df["timestamp"]):
        df["timestamp"] = pd.to_datetime(df["timestamp"])

    X = df[["event_type", "user", "ip"]].copy()
    pipe.fit(X)

    # scores: quanto menor, mais anômalo
    Xt = pipe.named_steps["pre"].transform(X)
    scores = pipe.named_steps["model"].decision_function(Xt)
    preds = pipe.named_steps["model"].predict(Xt)  # -1 = outlier

    out = df.copy()
    out["anomaly_score"] = scores
    out["is_anomaly"] = (preds == -1)
    return AnomalyResult(data=out, model=pipe.named_steps["model"])


def plot_scores(res_df: pd.DataFrame, show: bool = False, save_path: Optional[str] = None) -> None:
    # import local p/ só carregar matplotlib quando necessário
    import matplotlib.pyplot as plt

    s = res_df.sort_values("timestamp")
    plt.figure(figsize=(11, 4))
    plt.plot(s["timestamp"], s["anomaly_score"], label="Anomaly score")
    out = s[s["is_anomaly"]]
    if not out.empty:
        plt.scatter(out["timestamp"], out["anomaly_score"], marker="o", s=28, label="Anomalia", zorder=3)

    plt.title("Anomaly score ao longo do tempo (valores menores = mais anômalo)")
    plt.xlabel("Tempo")
    plt.ylabel("Score")
    plt.legend()
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=140)
        print(f"🖼️  Gráfico salvo em {save_path}")
    if show:
        plt.show()
    plt.close()


def main() -> None:
    ap = argparse.ArgumentParser(description="Detecção de anomalias em logs (IsolationForest).")
    ap.add_argument("--input", default="data/sample_logs.csv", help="CSV de entrada (padrão: data/sample_logs.csv)")
    ap.add_argument("--contamination", type=float, default=0.02, help="fração estimada de anomalias")
    ap.add_argument("--show", action="store_true", help="mostrar gráfico na tela")
    ap.add_argument("--plot", default=None, help="salvar gráfico em PNG (ex.: outputs/anomaly_scores.png)")
    args = ap.parse_args()

    df = pd.read_csv(args.input, parse_dates=["timestamp"])
    res = detect_anomalies(df, contamination=args.contamination)

    anomalies = res.data[res.data["is_anomaly"]].sort_values("anomaly_score")
    out_csv = "outputs/anomalies.csv"
    anomalies.to_csv(out_csv, index=False)
    print(f"✔️  {len(anomalies)} anomalias salvas em {out_csv}")

    if args.show or args.plot:
        plot_scores(res.data, show=args.show, save_path=args.plot)


if __name__ == "__main__":
    main()
