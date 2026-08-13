"""
Simio Aerospace - Fase 1 - Diagramas de precedencia (Joaco)
============================================================
Genera 5 diagramas de precedencia (uno por celda) a partir de 'Simio Aerospace
Data.xlsx', usando el campo Seq # como regla de precedencia: las tareas con el
mismo numero de secuencia se ejecutan en paralelo; un numero de secuencia mayor
solo puede iniciar cuando finaliza el anterior (igual que Task Sequence en Simio).

Nadie mas tiene asignados estos diagramas en la tabla de distribucion de
entregables, pero el enunciado los pide dentro del informe tecnico (seccion de
Documentacion de resultados, a cargo de Joaco).
"""
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import openpyxl

ROOT = Path(__file__).resolve().parents[2]
RAW_DATA = ROOT / "Simio Aerospace Data.xlsx"
OUT_DIR = Path(__file__).resolve().parent.parent / "graficas"
OUT_DIR.mkdir(exist_ok=True)

CELDAS_KEY = ["WorkCell1", "WorkCell2", "WorkCell3", "WorkCell4", "WorkCell5"]
CELDAS_LABEL = ["Celda 1", "Celda 2", "Celda 3", "Celda 4", "Celda 5"]

BLUE = "#2a78d6"
SURFACE = "#fcfcfb"
BOX_FILL = "#eaf1fc"
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#898781"

plt.rcParams.update({
    "figure.facecolor": SURFACE, "savefig.facecolor": SURFACE,
    "font.family": "sans-serif",
    "font.sans-serif": ["Segoe UI", "Arial", "DejaVu Sans"],
})


def load_workcell(ws):
    tasks = []
    for row in list(ws.iter_rows(values_only=True))[2:]:
        if row[0] is None or row[1] is None:
            continue
        tasks.append({"seq": int(row[0]), "task": str(row[1]).strip(), "mech": row[4]})
    return tasks


def wrap(text, width=18):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= width:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return "\n".join(lines)


def draw_precedence(celda_label, tasks, out_path):
    seqs = sorted(set(t["seq"] for t in tasks))
    grupos = {s: [t for t in tasks if t["seq"] == s] for s in seqs}
    max_altura = max(len(g) for g in grupos.values())

    box_w, box_h = 2.15, 0.62
    col_gap = 0.95
    row_gap = 0.18

    fig_w = len(seqs) * (box_w + col_gap) + 1.5
    fig_h = max_altura * (box_h + row_gap) + 1.6
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    ax.set_xlim(0, len(seqs) * (box_w + col_gap))
    ax.set_ylim(0, max_altura * (box_h + row_gap) + 0.6)
    ax.axis("off")

    centers = {}  # seq -> list of (x, y) centers for each task in the group
    for ci, s in enumerate(seqs):
        grupo = grupos[s]
        x = ci * (box_w + col_gap) + box_w / 2 + 0.3
        n = len(grupo)
        total_h = n * box_h + (n - 1) * row_gap
        y_top = (max_altura * (box_h + row_gap) - total_h) / 2 + total_h
        pts = []
        for ti, t in enumerate(grupo):
            y = y_top - ti * (box_h + row_gap) - box_h / 2
            box = FancyBboxPatch((x - box_w / 2, y - box_h / 2), box_w, box_h,
                                  boxstyle="round,pad=0.03,rounding_size=0.06",
                                  linewidth=1.1, edgecolor=BLUE, facecolor=BOX_FILL, zorder=3)
            ax.add_patch(box)
            label = f"{wrap(t['task'], 20)}\n({t['mech']} mec.)"
            ax.text(x, y, label, ha="center", va="center", fontsize=7.6, color=INK, zorder=4,
                    linespacing=1.15)
            pts.append((x, y))
        centers[s] = pts
        # etiqueta de secuencia arriba de la columna
        ax.text(x, max_altura * (box_h + row_gap) + 0.35, f"Seq. {s}",
                 ha="center", va="bottom", fontsize=10, fontweight="bold", color=INK2)

    # flechas entre columnas consecutivas (de cada nodo del grupo anterior a
    # cada nodo del grupo siguiente, agregadas por un punto medio para no saturar)
    for i in range(len(seqs) - 1):
        s_from, s_to = seqs[i], seqs[i + 1]
        x_from = max(p[0] for p in centers[s_from]) + box_w / 2
        x_to = min(p[0] for p in centers[s_to]) - box_w / 2
        y_from_mid = sum(p[1] for p in centers[s_from]) / len(centers[s_from])
        y_to_mid = sum(p[1] for p in centers[s_to]) / len(centers[s_to])
        arrow = FancyArrowPatch((x_from, y_from_mid), (x_to, y_to_mid),
                                 arrowstyle="-|>", mutation_scale=14,
                                 linewidth=1.3, color=MUTED, zorder=2,
                                 connectionstyle="arc3,rad=0.0")
        ax.add_patch(arrow)

    ax.set_title(f"Diagrama de precedencia — {celda_label}\n"
                 f"(tareas en la misma columna se ejecutan en paralelo; una columna "
                 f"solo inicia cuando termina la anterior)",
                 fontsize=11.5, fontweight="bold", color=INK, pad=14)
    fig.savefig(out_path, dpi=170, bbox_inches="tight")
    plt.close(fig)
    print(f"  -> {out_path.name}")


def main():
    wb = openpyxl.load_workbook(RAW_DATA, data_only=True)
    print("Generando diagramas de precedencia en", OUT_DIR)
    for key, label in zip(CELDAS_KEY, CELDAS_LABEL):
        tasks = load_workcell(wb[key])
        out_path = OUT_DIR / f"precedencia_{key.lower()}.png"
        draw_precedence(label, tasks, out_path)
    print("Listo.")


if __name__ == "__main__":
    main()
