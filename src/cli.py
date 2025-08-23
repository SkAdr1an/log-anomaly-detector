import argparse
import matplotlib.pyplot as plt
from log_anomaly_detector import detect_anomalies

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    parser.add_argument("--plot", type=str, required=True)
    parser.add_argument("--contamination", type=float, default=0.02)
    args = parser.parse_args()

    df = detect_anomalies(args.input, contamination=args.contamination)
    df.to_csv(args.output, index=False)
    print(f"Anomalias salvas em {args.output}")

    plt.figure(figsize=(12, 6))
    plt.plot(df["anomaly_score"], label="Anomaly Score")
    plt.axhline(y=0, color="r", linestyle="--")
    plt.legend()
    plt.savefig(args.plot)
    print(f"Gráfico salvo em {args.plot}")
