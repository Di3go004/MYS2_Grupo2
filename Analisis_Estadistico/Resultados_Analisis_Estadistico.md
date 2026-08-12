# Análisis estadístico de tiempos de trabajo: SA101 y SA102

## 1. Resultado general

> **Resultado principal:** al sumar las duraciones esperadas de las 83 tareas, SA101 presenta una carga acumulada de **399.603 horas** y SA102 de **379.900 horas**. SA102 requiere **19.703 horas menos**, equivalentes a una reducción de **4.93 %** frente a SA101.

De las **83 tareas comparadas**, **53 tienen la misma duración esperada**, **4 son semejantes** y **26 presentan diferencias mayores al 5 %**. Esto indica que la mayoría de las tareas se comporta igual en ambos productos, pero un grupo reducido explica las diferencias importantes entre SA101 y SA102.

La **Celda 2** concentra la mayor carga acumulada en los dos productos: **116.633 horas para SA101** y **116.657 horas para SA102**. Este comportamiento permite identificarla como el principal candidato preliminar a cuello de botella.

### Alcance del resultado

Las cifras anteriores representan la **suma de las duraciones esperadas de las tareas**. No equivalen al tiempo de ciclo ni al tiempo real de permanencia de un avión en la línea, debido a que existen tareas paralelas, relaciones de precedencia y restricciones de disponibilidad de mecánicos.

## 2. Metodología estadística

Los tiempos de trabajo se encuentran definidos mediante distribuciones triangulares de la forma $Triangular(a,m,b)$, donde $a$ es el valor mínimo, $m$ es la moda y $b$ es el valor máximo. Para cada tarea se calcularon las siguientes medidas:

- Media: $E(X)=(a+m+b)/3$.
- Varianza: $Var(X)=(a^2+m^2+b^2-am-ab-mb)/18$.
- Desviación estándar: $DE=\sqrt{Var(X)}$.
- Coeficiente de variación: $CV=(DE/E(X))\times100$.

En total se evaluaron **83 tareas** para cada producto. La comparación se realizó por tarea, secuencia y celda de trabajo. Se consideraron iguales las medias sin diferencia, semejantes las que presentaron una variación de hasta 5 % y diferentes las que superaron dicho porcentaje.

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

En conjunto, la menor carga de SA102 se explica principalmente por las reducciones observadas en las celdas 1 y 4. Por otra parte, la celda 2 requiere atención debido a que presenta la mayor carga esperada para ambos productos.

## 4. Semejanzas y diferencias por tarea

La comparación de medias permitió determinar cuáles actividades mantienen el mismo comportamiento y cuáles cambian según el producto. Las diferencias más relevantes se muestran a continuación:

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

La media se utilizó para identificar las tareas con mayor duración esperada, mientras que la desviación estándar permitió determinar cuáles presentan una mayor dispersión absoluta en sus tiempos.

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

Las tareas se clasificaron por separado dentro de cada celda y producto. Se consideró **alta** una duración o variabilidad ubicada en el cuartil superior (valor mayor o igual a Q3), **baja** si se ubicó en el cuartil inferior (valor menor o igual a Q1) y **media** para los valores intermedios. Una tarea se clasificó como **crítica** cuando presentó simultáneamente duración y variabilidad altas.

