# Log Anomaly Detector

Projeto de detecção de anomalias em logs usando Machine Learning (IsolationForest).

## Estrutura
- **scripts/** → Gerador de dados sintéticos
- **src/** → Código principal (detecção + CLI)
- **data/** → Dados de entrada (CSV)
- **outputs/** → Resultados (anomalias e gráficos)

## Como rodar

```bash
python -m venv .venv
.venv\Scripts\Activate
pip install -r requirements.txt

# Gerar dados de exemplo
python scripts/generate_sample_data.py --rows 2000 --out data/sample_logs.csv

# Rodar a detecção
python src/cli.py --input data/sample_logs.csv --output outputs/anomalies.csv --plot outputs/anomaly_scores.png --contamination 0.02
```

## Tecnologias
- Python
- Scikit-Learn
- Pandas
- Matplotlib
