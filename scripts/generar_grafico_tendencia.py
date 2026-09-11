"""
Genera el gráfico de tendencia mensual de m² bacheados a partir de
data/resumen_mensual_2026.csv

Uso:
    pip install matplotlib pandas
    python scripts/generar_grafico_tendencia.py
"""
import csv
import os

import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "resumen_mensual_2026.csv")
OUT_PATH = os.path.join(BASE_DIR, "data", "tendencia_m2_mensual.png")


def cargar_datos(path):
    meses, m2_mes = [], []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            meses.append(row["mes"])
            m2_mes.append(float(row["m2_mes"]))
    return meses, m2_mes


def graficar(meses, m2_mes, out_path):
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(meses, m2_mes, marker="o", color="#1f4e79")
    ax.fill_between(range(len(meses)), m2_mes, alpha=0.15, color="#1f4e79")
    for i, valor in enumerate(m2_mes):
        ax.annotate(f"{valor:,.0f}", (i, valor), textcoords="offset points",
                    xytext=(0, 8), ha="center", fontsize=9)
    ax.set_title("Tendencia mensual de m² bacheados")
    ax.set_ylabel("m² bacheados")
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    print(f"Gráfico guardado en: {out_path}")


if __name__ == "__main__":
    meses, m2_mes = cargar_datos(DATA_PATH)
    graficar(meses, m2_mes, OUT_PATH)
