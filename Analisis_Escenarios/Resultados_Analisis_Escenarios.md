# Análisis de escenarios y de resultados: lote inicial de 75 aviones

## 1. Definición del escenario

El lote inicial que se analiza está compuesto por 75 aviones: 45 unidades de
SA101 (60%) y 30 unidades de SA102 (40%), sin conocerse el orden exacto de
llegada. Para cada una de las cinco celdas de trabajo se calculó la carga total,
en horas-hombre, necesaria para fabricar el lote completo:

HH_lote(celda) = HH_esperadas_SA101(celda) x 45 + HH_esperadas_SA102(celda) x 30

usando las horas-hombre esperadas por avión que se obtuvieron en el análisis de
capacidad (media de cada tarea multiplicada por los mecánicos requeridos, sumada
por celda).

## 2. Carga del lote por celda

| Celda | HH por avión SA101 | HH por avión SA102 | HH totales del lote | % del total |
|---|---:|---:|---:|---:|
| Celda 1 | 254.70 | 214.17 | 17,886.5 | 21.7% |
| Celda 2 | 324.13 | 323.98 | 24,305.4 | 29.5% |
| Celda 3 | 224.35 | 228.29 | 16,944.4 | 20.6% |
| Celda 4 | 299.11 | 267.81 | 21,494.5 | 26.1% |
| Celda 5 | 24.00 | 24.00 | 1,800.0 | 2.2% |
| Total | | | 82,430.8 | 100% |

La Celda 2 concentra casi el 30% de toda la mano de obra que exige el lote,
consistente con el resultado del análisis estadístico, donde ya aparecía como la
celda con mayor carga esperada por avión. La Celda 4 es la segunda con mayor
carga (26.1%) y es además la única celda donde la demanda de mecánicos alcanza el
límite de 8 disponibles en al menos una secuencia. La Celda 5 tiene una
participación marginal, de apenas 2.2% del total.

## 3. Carga del lote frente a la capacidad teórica disponible

La duración de calendario que exige el lote bajo la política actual de ciclo fijo
se calcula como:

Duración de calendario = (75-1) x 4 + 5 celdas x 4 = 316 días (aproximadamente
63 semanas), contando el tiempo entre la entrada del primer avión y la salida del
último de la Celda 5, con el sistema arrancando vacío e inactivo.

Comparando la carga de cada celda contra la capacidad teórica de 120
horas-hombre por día (8 mecánicos x 15 horas efectivas), se obtiene la
utilización teórica de mano de obra durante esos 316 días:

| Celda | HH del lote | Días necesarios solo con mano de obra | Utilización teórica en 316 días |
|---|---:|---:|---:|
| Celda 1 | 17,886.5 | 149.1 | 47.2% |
| Celda 2 | 24,305.4 | 202.5 | 64.1% |
| Celda 3 | 16,944.4 | 141.2 | 44.7% |
| Celda 4 | 21,494.5 | 179.1 | 56.7% |
| Celda 5 | 1,800.0 | 15.0 | 4.7% |

Incluso la celda con mayor carga, la Celda 2, utiliza apenas el 64% de su
capacidad teórica durante el tiempo que dura el lote bajo el cronograma actual.
Esto indica que la mano de obra disponible no es, en términos agregados, la
restricción del sistema: sobra capacidad instalada de mecánicos en las cinco
celdas a lo largo de todo el lote.

## 4. La restricción real: la ventana del ciclo fijo

Si la mano de obra sobra a nivel de lote, la razón por la que el caso describe un
sistema con trabajo desplazado hay que buscarla no en el total de horas
disponibles, sino en cuánto trabajo cabe dentro de un solo ciclo de 4 días. Un
ciclo de 4 días equivale a 60 horas efectivas de trabajo por celda (15 horas
efectivas por día, considerando los dos turnos activos). Comparando esa ventana
contra la duración real que necesita un avión para completar todas sus tareas en
cada celda, respetando las precedencias y el paralelismo con 8 mecánicos:

| Celda | Duración real SA101 | Duración real SA102 | Ventana disponible | Trabajo desplazado SA101 | Trabajo desplazado SA102 |
|---|---:|---:|---:|---:|---:|
| Celda 1 | 79.9 h | 65.5 h | 60 h | 19.9 h (25%) | 5.5 h (8%) |
| Celda 2 | 102.5 h | 100.7 h | 60 h | 42.5 h (41%) | 40.7 h (40%) |
| Celda 3 | 67.9 h | 70.3 h | 60 h | 7.8 h (12%) | 10.3 h (15%) |
| Celda 4 | 75.9 h | 67.7 h | 60 h | 15.9 h (21%) | 7.7 h (11%) |
| Celda 5 | 6.4 h | 6.4 h | 60 h | 0 h (0%) | 0 h (0%) |

Cuatro de las cinco celdas no alcanzan a terminar el trabajo de un avión dentro
de la ventana de 4 días, por lo que generan trabajo desplazado en cada ciclo y no
solo de forma ocasional. La Celda 2 es la más afectada: entre el 40% y el 41% de
su carga por avión se traslada de forma sistemática hacia la Celda 3. La Celda 5
es la única que siempre termina a tiempo, con un margen amplio dentro de su
ventana.

## 5. Cuellos de botella y riesgos identificados

Cruzando la carga por celda, la demanda de mecánicos por secuencia y el
porcentaje de trabajo desplazado por ciclo, se ordenan las celdas de la
siguiente manera:

| Celda | Carga del lote | Mecánicos pico | Trabajo desplazado por ciclo | Diagnóstico |
|---|---|---|---|---|
| Celda 2 | 29.5% (la mayor) | 7 de 8 | 40-41% | Cuello de botella principal |
| Celda 4 | 26.1% (segunda) | 8 de 8, sin margen | 11-21% | Restricción de mecánicos |
| Celda 1 | 21.7% | 7 de 8 | 8-25% | Riesgo moderado |
| Celda 3 | 20.6% | 7 de 8 | 12-15% | Riesgo moderado |
| Celda 5 | 2.2% | 5 de 8 | 0% | Riesgo de inactividad |

La Celda 2 es la única que aparece entre las más críticas en las tres
dimensiones a la vez: mayor carga por avión, mayor carga del lote completo, mayor
utilización teórica y mayor porcentaje de trabajo desplazado por ciclo. Dentro de
esta celda, la tarea "Operator turn table and rotate to position" (secuencia 3,
alrededor de 18 horas en ambos productos) representa por sí sola casi un tercio
de la ventana de 60 horas del ciclo.

La Celda 4 concentra su riesgo en la disponibilidad de mecánicos: en la secuencia
3 exige exactamente 8 mecánicos simultáneos, el límite disponible, sin ningún
margen. Cualquier variación al alza en los tiempos de tarea o la futura
incorporación del SA103 podría llevarla por encima de la capacidad disponible.

La Celda 5, en el extremo opuesto, usa apenas el 4.7% de su capacidad teórica y
tiene el menor pico de mecánicos del sistema (5 de 8). No representa un riesgo de
saturación sino de inactividad: bajo la política actual el avión simplemente
espera en la celda hasta que se cumple el ciclo, con los mecánicos ociosos
durante buena parte del tiempo.

Con cuatro de las cinco celdas generando trabajo desplazado en cada ciclo, la
acumulación de trabajo pendiente que se traslada de celda en celda es estructural
bajo la política actual y no un evento ocasional, lo que respalda la necesidad de
evaluar la alternativa donde el avión avanza solo cuando termina el trabajo de la
celda, tal como plantea el caso.

Un riesgo adicional a considerar hacia la Fase 3: el SA103 se asumirá con los
mismos tiempos que SA101 y su incorporación reduce el ciclo objetivo de 4 a 3.5
días. Dado que SA101 es, en la mayoría de las celdas, el producto más lento o
similar al más lento, esa combinación de mayor carga y menor ventana
probablemente agravaría el desbalance ya detectado en las Celdas 2 y 4.

## 6. Supuestos utilizados

- El tiempo esperado de cada tarea se calcula como la media de la distribución
  triangular (a+m+b)/3, tal como se usó en el análisis estadístico y de
  capacidad.
- La duración esperada por celda toma el máximo de las tareas que comparten
  número de secuencia, dado que el campo Seq# implementa precedencia en
  paralelo, no en serie.
- La ventana efectiva por ciclo se calcula con 15 horas efectivas por día (turno
  1: 8 horas, turno 2: 7 horas), ya que el tercer turno no opera actualmente.
- Para el lote de 75 aviones se asume la mezcla exacta de 60% SA101 y 40% SA102,
  sin considerar el orden de llegada, ya que el objetivo es comparar carga
  agregada y no simular el flujo.
- La duración de calendario de 316 días es una estimación teórica de esta fase y
  no sustituye la simulación: no incorpora bloqueos ni esperas que sí capturará
  el modelo de Simio en la Fase 2.
- El SA103 y el lote de 100 aviones no se cuantifican en este análisis; se dejan
  mencionados como riesgo cualitativo para la Fase 3.

## 7. KPIs propuestos para el modelo de Simio (Fase 2)

- Tiempo de ciclo real, para verificar si el sistema sostiene los 4 días por
  avión sin acumular atraso.
- Trabajo desplazado por celda y por ciclo, para contrastar directamente contra
  los porcentajes estimados en la sección 4.
- Utilización de mecánicos por celda y turno, para confirmar si la Celda 2 y la
  Celda 4 son efectivamente las más ocupadas.
- Trabajo en proceso promedio y máximo por celda.
- Tiempo de finalización del lote, comparado contra los 316 días estimados de
  forma teórica.
- Bloqueo e inanición por celda, para verificar si la Celda 5 efectivamente pasa
  tiempo inactiva esperando el ciclo.
- Porcentaje de secuencias que exceden los 8 mecánicos disponibles, para
  verificar el comportamiento de la Celda 4 bajo variabilidad real.

Al construir el modelo funcional se recomienda instrumentar el trabajo
desplazado por celda desde el primer build, priorizar la validación de los
distintos casos de buffer en la Celda 2 y la Celda 4, y evaluar la reasignación
de mecánicos ociosos de la Celda 5 hacia la Celda 2 antes de simular un pool de
trabajadores totalmente flexible.
