# scripts/analyze_anomalies.py
import argparse
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

OUTPUT_DIR = Path("outputs")
ANOMALIES_CSV = OUTPUT_DIR / "anomalies.csv"
RESUMO_CSV = OUTPUT_DIR / "resumo_anomalias.csv"
PNG_USUARIOS = OUTPUT_DIR / "anomalias_por_usuario.png"
PNG_EVENTOS = OUTPUT_DIR / "anomalias_por_evento.png"


def main():
    ap = argparse.ArgumentParser(
        description="Analisa o arquivo outputs/anomalies.csv e gera relatórios e gráficos."
    )
    ap.add_argument("--show", action="store_true", help="Mostrar gráficos na tela (opcional).")
    args = ap.parse_args()

    # 1) Garantir pasta de saída
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 2) Ler arquivo de anomalias
    if not ANOMALIES_CSV.exists():
        raise FileNotFoundError(
            f"Não encontrei {ANOMALIES_CSV}. Rode antes: "
            "python src/log_anomaly_detector.py --plot outputs/anomaly_scores.png"
        )
    anomalias = pd.read_csv(ANOMALIES_CSV)

    print("Primeiras linhas:")
    print(anomalias.head())

    # 3) Estatísticas e resumo
    print("\nResumo estatístico (anomaly_score):")
    print(anomalias["anomaly_score"].describe())

    por_usuario = anomalias["user"].value_counts()
    por_evento = anomalias["event_type"].value_counts()
    por_ip = anomalias["ip"].value_counts()

    # salva resumo “wide” em CSV
    resumo = pd.DataFrame({
        "anomalias_por_usuario": por_usuario,
        "anomalias_por_evento": por_evento,
        "anomalias_por_ip": por_ip
    })
    resumo.to_csv(RESUMO_CSV, encoding="utf-8")
    print(f"\n✅ Resumo salvo em {RESUMO_CSV.as_posix()}")

    # 4) Gráficos em PNG
    ax = por_usuario.plot(kind="bar", figsize=(10, 4), title="Anomalias por Usuário")
    ax.set_xlabel("Usuário"); ax.set_ylabel("Quantidade")
    plt.tight_layout()
    plt.savefig(PNG_USUARIOS, dpi=140)
    print(f"🖼️  Gráfico salvo em {PNG_USUARIOS.as_posix()}")
    if args.show:
        plt.show()
    plt.close()

    ax = por_evento.plot(kind="bar", figsize=(10, 4), title="Anomalias por Tipo de Evento")
    ax.set_xlabel("Evento"); ax.set_ylabel("Quantidade")
    plt.tight_layout()
    plt.savefig(PNG_EVENTOS, dpi=140)
    print(f"🖼️  Gráfico salvo em {PNG_EVENTOS.as_posix()}")
    if args.show:
        plt.show()
    plt.close()


if __name__ == "__main__":
    main()
