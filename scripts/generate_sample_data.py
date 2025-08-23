import pandas as pd
import numpy as np
import argparse
from datetime import datetime, timedelta
import random

def generate_logs(n_rows=1000):
    base_time = datetime.now()
    users = ["alice", "bob", "charlie", "david"]
    events = ["login_success", "login_fail", "file_access", "config_change"]
    ips = [f"192.168.0.{i}" for i in range(1, 20)]

    data = []
    for i in range(n_rows):
        row = {
            "timestamp": (base_time + timedelta(seconds=i*30)).strftime("%Y-%m-%d %H:%M:%S"),
            "user": random.choice(users),
            "event_type": random.choice(events),
            "ip": random.choice(ips)
        }
        data.append(row)

    return pd.DataFrame(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int, default=1000)
    parser.add_argument("--out", type=str, default="data/sample_logs.csv")
    args = parser.parse_args()

    df = generate_logs(args.rows)
    df.to_csv(args.out, index=False)
    print(f"Arquivo gerado em {args.out}")
