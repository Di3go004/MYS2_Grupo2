# Análisis estadístico de tiempos de trabajo: SA101 y SA102

## 1. Resultado general

> **Resultado principal:** al sumar las duraciones esperadas de las 83 tareas, SA101 presenta una carga acumulada de **399.603 horas** y SA102 de **379.900 horas**. SA102 requiere **19.703 horas menos**, equivalentes a una reducción de **4.93 %** frente a SA101.

De las **83 tareas comparadas**, **53 tienen la misma duración esperada**, **4 son semejantes** y **26 presentan diferencias mayores al 5 %**. Esto indica que la mayoría de las tareas se comporta igual en ambos productos, pero un grupo reducido explica las diferencias importantes entre SA101 y SA102.

La **Celda 2** concentra la mayor carga acumulada en los dos productos: **116.633 horas para SA101** y **116.657 horas para SA102**. Por ello, es el principal candidato estadístico a cuello de botella y deberá comprobarse posteriormente en Simio.

### Interpretación correcta

Estas cifras representan la **suma de las duraciones esperadas de las tareas**. No son el tiempo de ciclo ni el tiempo real que tarda un avión en atravesar la línea, porque algunas tareas se ejecutan en paralelo y existen precedencias y restricciones de mecánicos.

## 2. Relación con el enunciado de la Fase 1

El análisis se realizó con base en los tres entregables de **análisis estadístico** indicados en las páginas 10 y 11 del enunciado oficial:

1. Calcular media, varianza, desviación estándar y coeficiente de variación para cada tarea de SA101 y SA102.
2. Comparar los productos por tarea, número de secuencia y celda de trabajo.
3. Identificar y clasificar las tareas con mayor duración esperada y mayor variabilidad dentro de cada celda.

Se procesaron **83 tareas**, distribuidas en las cinco hojas `WorkCell1` a `WorkCell5`. En el Excel fuente, `Part Type1` corresponde a **SA101** y `PartType2` a **SA102**.

## 3. Comparación por celda

| Celda | Tareas | Carga SA101 (h) | Carga SA102 (h) | Cambio de SA102 | Menor carga | Mayor dispersión |
|---|---:|---:|---:|---:|---|---|
| Celda 1 | 19 | 94.333 | 79.850 | -15.35% | SA102 | SA101 |
| Celda 2 | 20 | 116.633 | 116.657 | +0.02% | SA101 | SA102 |
| Celda 3 | 19 | 87.150 | 90.213 | +3.52% | SA101 | SA102 |
| Celda 4 | 20 | 90.587 | 82.280 | -9.17% | SA102 | SA101 |
| Celda 5 | 5 | 10.900 | 10.900 | +0.00% | Igual | Iguales |

### Lectura de los resultados por celda

- **Celda 1:** SA102 reduce la carga esperada en 15.35 %. Es la mayor reducción entre ambos productos.
- **Celda 2:** las cargas son prácticamente iguales; SA102 solo aumenta 0.02 %.
- **Celda 3:** SA102 aumenta la carga en 3.52 %, por lo que SA101 tiene una ligera ventaja.
- **Celda 4:** SA102 reduce la carga esperada en 9.17 %.
- **Celda 5:** no existen diferencias entre los productos.

**Conclusión por celda:** la ventaja acumulada de SA102 se origina principalmente en las celdas 1 y 4. La celda 2 merece atención prioritaria porque posee la carga más alta para ambos productos.

## 4. Semejanzas y diferencias por tarea

Se utilizó el siguiente criterio de lectura: diferencia igual a 0 % = **igual**; diferencia de hasta 5 % = **semejante**; diferencia mayor a 5 % = **diferente**.

Las diferencias más relevantes son:

| Celda | Sec. | Tarea | SA101 (h) | SA102 (h) | Cambio SA102 | Menor carga |
|---|---:|---|---:|---:|---:|---|
| Celda 2 | 5 | Drill Pilot hole | 1.000 | 2.433 | +143.33% | SA101 |
| Celda 3 | 7 | Robot Syncing | 3.833 | 6.233 | +62.61% | SA101 |
| Celda 1 | 9 | Fillet Relef Bulkhead | 24.400 | 11.500 | -52.87% | SA102 |
| Celda 3 | 4 | Tools dump Zone 2 Clamps | 2.000 | 2.867 | +43.33% | SA101 |
| Celda 3 | 10 | Robot Syncing | 1.700 | 2.280 | +34.12% | SA101 |
| Celda 4 | 9 | Press button | 1.700 | 2.280 | +34.12% | SA101 |
| Celda 1 | 3 | Guide Splice Operation | 1.800 | 1.217 | -32.41% | SA102 |
| Celda 4 | 3 | Locate & close clip | 20.000 | 14.833 | -25.83% | SA102 |
| Celda 3 | 3 | Install Tack Fastener | 1.800 | 1.380 | -23.33% | SA102 |
| Celda 4 | 3 | Close Manual clamps | 1.800 | 1.380 | -23.33% | SA102 |

La diferencia porcentual más grande aparece en `Drill Pilot hole` de la celda 2, porque SA102 aumenta de 1.000 a 2.433 horas. Sin embargo, la diferencia absoluta que más reduce la carga general corresponde a `Fillet Relef Bulkhead` de la celda 1: SA102 requiere 12.900 horas menos que SA101.

## 5. Tareas de mayor duración y variabilidad

La **media** identifica las tareas que normalmente demandan más tiempo. La **desviación estándar (DE)** identifica las tareas cuyo tiempo puede fluctuar más en términos absolutos.

| Celda | Producto | Tarea de mayor duración | Media | Tarea de mayor variabilidad | DE |
|---|---|---|---:|---|---:|
| Celda 1 | SA101 | Fillet Relef Bulkhead (seq. 9) | 24.400 | Fillet Relef Bulkhead (seq. 9) | 1.257 |
| Celda 1 | SA102 | Load drill bars (seq. 4) | 16.000 | Fillet Relef Bulkhead (seq. 9) | 1.021 |
| Celda 2 | SA101 | Operator turn table and rotate to position (seq. 3) | 18.000 | Measure gap (seq. 10) | 1.161 |
| Celda 2 | SA102 | Operator turn table and rotate to position (seq. 3) | 18.000 | Measure gap (seq. 10) | 1.161 |
| Celda 3 | SA101 | Tool dump Zone 8 Clamps (seq. 9) | 17.917 | Drill 8 holes (seq. 6) | 1.027 |
| Celda 3 | SA102 | Tool dump Zone 8 Clamps (seq. 9) | 17.917 | Drill 8 holes (seq. 6) | 1.027 |
| Celda 4 | SA101 | Locate & close clip (seq. 3) | 20.000 | Remove BLKD assys (seq. 6) | 1.027 |
| Celda 4 | SA102 | Attach MHE (seq. 9) | 17.917 | Remove BLKD assys (seq. 6) | 1.027 |
| Celda 5 | SA101 | Perform local drill (seq. 2) | 2.500 | Perform local drill (seq. 2) | 0.102 |
| Celda 5 | SA102 | Perform local drill (seq. 2) | 2.500 | Perform local drill (seq. 2) | 0.102 |

### Clasificación utilizada

Las tareas se clasificaron por separado dentro de cada celda y producto. Se consideró **alta** una duración o variabilidad ubicada en el cuartil superior (valor mayor o igual a Q3), **baja** si está en el cuartil inferior (menor o igual a Q1) y **media** para los valores intermedios. Una tarea se marcó como **crítica** cuando fue alta tanto en duración como en variabilidad. El detalle completo está en la hoja `Clasificacion_Tareas` del Excel.

## Archivos de respaldo

- `Resultados_Analisis_Estadistico_Fase1.xlsx`: cálculos completos por tarea, secuencia y celda.
- `Simio Aerospace Data.xlsx`: datos originales utilizados.
