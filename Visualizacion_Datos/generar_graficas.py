"""
Simio Aerospace - Fase 1 - Visualizacion de datos (Joaco)
============================================================
Genera las graficas comparativas del entregable "Visualizacion de datos":
tiempos, variabilidad, carga de trabajo, demanda de mecanicos y capacidad
disponible, entre celdas y entre productos (SA101 / SA102).

Paleta: paleta categorica validada (colorblind-safe) del skill de dataviz del
equipo. Orden fijo de series, una sola tonalidad para magnitudes, sin doble eje.

Lee `resumen_escenarios.json` (generado por analisis_escenarios.py) y
'Simio Aerospace Data.xlsx' (para el detalle de variabilidad por tarea).
"""
import json
import math
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import openpyxl

ROOT = Path(__file__).resolve().parents[2]
RAW_DATA = ROOT / "Simio Aerospace Data.xlsx"
ANALISIS_DIR = Path(__file__).resolve().parent
JSON_PATH = ANALISIS_DIR / "resumen_escenarios.json"
OUT_DIR = ANALISIS_DIR.parent / "graficas"
OUT_DIR.mkdir(exist_ok=True)

# --- Paleta categorica validada (light mode, referencia del skill dataviz) --
BLUE = "#2a78d6"      # slot 1 -> SA101 / serie principal
ORANGE = "#eb6834"    # slot 2 -> SA102 / serie secundaria
AQUA = "#1baf7a"       # slot 3
YELLOW = "#eda100"    # slot 4
MAGENTA = "#e87ba4"   # slot 5
CRITICAL = "#d03b3b"  # status: excede limite / riesgo
GOOD = "#0ca30c"      # status: dentro de limite
MUTED = "#898781"     # ejes / texto secundario
GRID = "#e1e0d9"
INK = "#0b0b0b"
INK2 = "#52514e"
SURFACE = "#fcfcfb"

CELDA_COLORS = [BLUE, ORANGE, AQUA, YELLOW, MAGENTA]
CELDAS_LABEL = ["Celda 1", "Celda 2", "Celda 3", "Celda 4", "Celda 5"]
CELDAS_KEY = ["WorkCell1", "WorkCell2", "WorkCell3", "WorkCell4", "WorkCell5"]

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "font.family": "sans-serif",
    "font.sans-serif": ["Segoe UI", "Arial", "DejaVu Sans"],
    "text.color": INK, "axes.labelcolor": INK2, "axes.edgecolor": GRID,
    "xtick.color": INK2, "ytick.color": INK2,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "axes.axisbelow": True, "font.size": 11,
})


def style_axes(ax, y_grid_only=True):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color(MUTED)
    if y_grid_only:
        ax.grid(axis="y")
        ax.grid(axis="x", visible=False)
    ax.tick_params(length=0)


def savefig(fig, name):
    path = OUT_DIR / name
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    print(f"  -> {path.name}")


TRI_RE = re.compile(r"Random\.Triangular\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*\)")


def tri_stats(expr):
    a, m, b = (float(x) for x in TRI_RE.search(str(expr)).groups())
    mean = (a + m + b) / 3
    var = (a**2 + m**2 + b**2 - a*m - a*b - m*b) / 18
    sd = math.sqrt(var)
    cv = (sd / mean * 100) if mean else 0
    return mean, sd, cv


def load_all_tasks():
    wb = openpyxl.load_workbook(RAW_DATA, data_only=True)
    tasks = []
    for i, key in enumerate(CELDAS_KEY):
        ws = wb[key]
        for row in list(ws.iter_rows(values_only=True))[2:]:
            if row[0] is None or row[1] is None:
                continue
            seq, name, lh1, lh2, mech = row[0], row[1], row[2], row[3], row[4]
            m1, sd1, cv1 = tri_stats(lh1)
            m2, sd2, cv2 = tri_stats(lh2)
            tasks.append({"celda": CELDAS_LABEL[i], "celda_idx": i, "seq": seq,
                           "task": str(name).strip(), "mech": mech,
                           "sa101_mean": m1, "sa101_sd": sd1, "sa101_cv": cv1,
                           "sa102_mean": m2, "sa102_sd": sd2, "sa102_cv": cv2})
    return tasks


def grouped_bar(ax, labels, series, colors, series_labels, ylabel, value_fmt="{:.0f}"):
    n_series = len(series)
    n_groups = len(labels)
    width = 0.8 / n_series
    x = range(n_groups)
    for i, (vals, color, slabel) in enumerate(zip(series, colors, series_labels)):
        offs = [xi + (i - (n_series - 1) / 2) * width for xi in x]
        bars = ax.bar(offs, vals, width=width * 0.92, color=color, label=slabel,
                       edgecolor=SURFACE, linewidth=0.6)
        for b, v in zip(bars, vals):
            ax.text(b.get_x() + b.get_width() / 2, b.get_height(),
                    value_fmt.format(v), ha="center", va="bottom",
                    fontsize=8.5, color=INK2)
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.set_ylabel(ylabel)
    style_axes(ax)
    if n_series > 1:
        ax.legend(frameon=False, loc="upper right", ncols=n_series)


def main():
    resumen = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    base = resumen["por_celda_base"]
    escenario = resumen["escenario_lote_75"]
    params = resumen["parametros"]

    print("Generando graficas en", OUT_DIR)

    # === 1. Carga esperada por celda (Calculo 1): SA101 vs SA102 ===========
    fig, ax = plt.subplots(figsize=(8, 4.5))
    v101 = [base[c]["carga101"] for c in CELDAS_KEY]
    v102 = [base[c]["carga102"] for c in CELDAS_KEY]
    grouped_bar(ax, CELDAS_LABEL, [v101, v102], [BLUE, ORANGE], ["SA101", "SA102"],
                "Carga esperada por avion (horas)", "{:.0f}")
    ax.set_title("Carga de trabajo esperada por celda y producto", loc="left",
                  fontsize=13, fontweight="bold", color=INK)
    fig.suptitle("", fontsize=1)
    savefig(fig, "01_carga_esperada_por_celda.png")

    # === 2. Horas-hombre esperadas por avion (Calculo 2) ====================
    fig, ax = plt.subplots(figsize=(8, 4.5))
    hh101 = [base[c]["hh101"] for c in CELDAS_KEY]
    hh102 = [base[c]["hh102"] for c in CELDAS_KEY]
    grouped_bar(ax, CELDAS_LABEL, [hh101, hh102], [BLUE, ORANGE], ["SA101", "SA102"],
                "Horas-hombre esperadas por avion", "{:.0f}")
    ax.set_title("Horas-hombre requeridas por avion, por celda", loc="left",
                  fontsize=13, fontweight="bold", color=INK)
    savefig(fig, "02_horas_hombre_por_avion.png")

    # === 3. Carga del lote de 75 aviones por celda (magnitud, un solo hue) ==
    fig, ax = plt.subplots(figsize=(8, 4.5))
    hh_lote = [escenario[c]["hh_lote"] for c in CELDAS_KEY]
    max_idx = hh_lote.index(max(hh_lote))
    colors = [CRITICAL if i == max_idx else BLUE for i in range(5)]
    bars = ax.bar(CELDAS_LABEL, hh_lote, color=colors, edgecolor=SURFACE, width=0.6)
    for b, v, pct in zip(bars, hh_lote, [escenario[c]["pct_del_total_lote"] for c in CELDAS_KEY]):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height(),
                f"{v:,.0f} HH\n({pct:.0f}%)", ha="center", va="bottom", fontsize=9, color=INK2)
    ax.set_ylabel("Horas-hombre totales del lote")
    ax.set_title(f"Carga de trabajo del lote inicial de {params['lote_total']} aviones "
                 f"({params['n_sa101']} SA101 + {params['n_sa102']} SA102), por celda",
                 loc="left", fontsize=12.5, fontweight="bold", color=INK)
    style_axes(ax)
    ax.margins(y=0.15)
    fig.text(0.01, -0.02, "Celda 2 (en rojo) concentra la mayor carga de mano de obra del lote.",
              fontsize=9, color=INK2)
    savefig(fig, "03_carga_lote_75_aviones.png")

    # === 4. Riesgo de trabajo desplazado (hallazgo clave) ===================
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    dur101 = [escenario[c]["duracion_avion_sa101_h"] for c in CELDAS_KEY]
    dur102 = [escenario[c]["duracion_avion_sa102_h"] for c in CELDAS_KEY]
    n = len(CELDAS_LABEL)
    width = 0.35
    x = range(n)
    b1 = ax.bar([xi - width/2 for xi in x], dur101, width=width*0.92, color=BLUE,
                label="Duracion SA101", edgecolor=SURFACE, linewidth=0.6)
    b2 = ax.bar([xi + width/2 for xi in x], dur102, width=width*0.92, color=ORANGE,
                label="Duracion SA102", edgecolor=SURFACE, linewidth=0.6)
    ventana = params["dias_calendario_lote_ciclo_fijo"]  # not used here
    ventana_h = 60  # 4 dias x 15 h efectivas (ver Parametros)
    ax.axhline(ventana_h, color=CRITICAL, linewidth=1.6, linestyle="--", zorder=0)
    ax.text(n - 0.6, ventana_h + 1.5, "Ventana del ciclo fijo: 60 h (4 dias)",
            color=CRITICAL, fontsize=9, fontweight="bold")
    for bars, vals in [(b1, dur101), (b2, dur102)]:
        for b, v in zip(bars, vals):
            ax.text(b.get_x() + b.get_width()/2, b.get_height(), f"{v:.0f}",
                    ha="center", va="bottom", fontsize=8.5, color=INK2)
    ax.set_xticks(list(x)); ax.set_xticklabels(CELDAS_LABEL)
    ax.set_ylabel("Duracion esperada por avion (horas)")
    ax.set_title("Duracion real de un avion en cada celda vs. ventana del ciclo fijo (4 dias)",
                 loc="left", fontsize=12.5, fontweight="bold", color=INK)
    style_axes(ax)
    ax.legend(frameon=False, loc="upper left")
    fig.text(0.01, -0.03,
              "Toda barra por encima de la linea roja implica trabajo que la politica actual "
              "'desplaza' hacia la siguiente celda cada ciclo (excepto Celda 5).",
              fontsize=9, color=INK2)
    savefig(fig, "04_riesgo_trabajo_desplazado.png")

    # === 5. Demanda pico de mecanicos por celda vs capacidad disponible =====
    fig, ax = plt.subplots(figsize=(8, 4.5))
    picos = [base[c]["pico_mecanicos"] for c in CELDAS_KEY]
    colors = [CRITICAL if p >= 8 else (YELLOW if p >= 7 else BLUE) for p in picos]
    bars = ax.bar(CELDAS_LABEL, picos, color=colors, width=0.55, edgecolor=SURFACE)
    ax.axhline(8, color=INK2, linewidth=1.4, linestyle="--")
    ax.text(4.55, 8.08, "Capacidad: 8 mecanicos", color=INK2, fontsize=9, ha="right")
    for b, v in zip(bars, picos):
        ax.text(b.get_x() + b.get_width()/2, b.get_height(), f"{v}/8",
                ha="center", va="bottom", fontsize=9.5, color=INK2, fontweight="bold")
    ax.set_ylim(0, 9.5)
    ax.set_ylabel("Mecanicos simultaneos (pico)")
    ax.set_title("Demanda pico de mecanicos por celda (peor secuencia) vs. capacidad de 8",
                 loc="left", fontsize=12.5, fontweight="bold", color=INK)
    style_axes(ax)
    savefig(fig, "05_demanda_pico_mecanicos.png")

    # === 6. Utilizacion teorica de mano de obra bajo el ciclo fijo actual ===
    fig, ax = plt.subplots(figsize=(8, 4.5))
    util = [escenario[c]["utilizacion_bajo_ciclo_fijo_pct"] for c in CELDAS_KEY]
    colors = [BLUE for _ in util]
    bars = ax.bar(CELDAS_LABEL, util, color=colors, width=0.55, edgecolor=SURFACE)
    for b, v in zip(bars, util):
        ax.text(b.get_x() + b.get_width()/2, b.get_height(), f"{v:.0f}%",
                ha="center", va="bottom", fontsize=9.5, color=INK2, fontweight="bold")
    ax.set_ylim(0, 100)
    ax.set_ylabel(f"% de la capacidad usada en {params['dias_calendario_lote_ciclo_fijo']} dias")
    ax.set_title("Utilizacion teorica de la mano de obra bajo el cronograma actual\n"
                 "(ciclo fijo de 4 dias/avion, lote de 75 aviones)",
                 loc="left", fontsize=12.5, fontweight="bold", color=INK)
    style_axes(ax)
    fig.text(0.01, -0.03,
              "Incluso la celda mas cargada usa una fraccion de su capacidad disponible: "
              "la mano de obra no es la restriccion bajo la politica actual.",
              fontsize=9, color=INK2)
    savefig(fig, "06_utilizacion_teorica_ciclo_fijo.png")

    # === 7. Variabilidad: top 12 tareas con mayor desviacion estandar =======
    tasks = load_all_tasks()
    top = sorted(tasks, key=lambda t: max(t["sa101_sd"], t["sa102_sd"]), reverse=True)[:12]
    top = top[::-1]  # para que el mayor quede arriba en barh
    fig, ax = plt.subplots(figsize=(8.5, 6))
    labels = [f"{t['celda']} · {t['task'][:28]}" for t in top]
    sd101 = [t["sa101_sd"] for t in top]
    sd102 = [t["sa102_sd"] for t in top]
    y = range(len(top))
    h = 0.35
    ax.barh([yi + h/2 for yi in y], sd101, height=h*0.9, color=BLUE, label="SA101")
    ax.barh([yi - h/2 for yi in y], sd102, height=h*0.9, color=ORANGE, label="SA102")
    ax.set_yticks(list(y)); ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlabel("Desviacion estandar (horas)")
    ax.set_title("Tareas con mayor variabilidad de tiempo (top 12, todas las celdas)",
                 loc="left", fontsize=12.5, fontweight="bold", color=INK)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.grid(axis="x", color=GRID); ax.grid(axis="y", visible=False)
    ax.tick_params(length=0)
    ax.legend(frameon=False, loc="lower right")
    savefig(fig, "07_top_variabilidad_tareas.png")

    # === 8. Coeficiente de variacion promedio por celda ======================
    fig, ax = plt.subplots(figsize=(8, 4.5))
    cv_por_celda = {c: [] for c in CELDAS_LABEL}
    for t in tasks:
        cv_por_celda[t["celda"]].append((t["sa101_cv"] + t["sa102_cv"]) / 2)
    cv_avg = [sum(v)/len(v) for v in (cv_por_celda[c] for c in CELDAS_LABEL)]
    bars = ax.bar(CELDAS_LABEL, cv_avg, color=CELDA_COLORS, width=0.55, edgecolor=SURFACE)
    for b, v in zip(bars, cv_avg):
        ax.text(b.get_x() + b.get_width()/2, b.get_height(), f"{v:.0f}%",
                ha="center", va="bottom", fontsize=9.5, color=INK2, fontweight="bold")
    ax.set_ylabel("Coeficiente de variacion promedio")
    ax.set_title("Variabilidad relativa promedio de los tiempos de tarea, por celda",
                 loc="left", fontsize=12.5, fontweight="bold", color=INK)
    style_axes(ax)
    savefig(fig, "08_cv_promedio_por_celda.png")

    print("\nListo. 8 graficas generadas en", OUT_DIR)


if __name__ == "__main__":
    main()
