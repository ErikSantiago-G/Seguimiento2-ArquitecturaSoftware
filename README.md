# MapReduce: Análisis nutricional de alimentos

Ejercicio de **MapReduce** en Python que analiza un dataset con la composición nutricional de distintos alimentos (calorías, proteínas, grasas, minerales y vitaminas).

## Preguntas que resuelve

1. ¿Qué alimento tiene la mayor cantidad de grasas?
2. ¿Qué alimento tiene la mayor cantidad de vitamina C?
3. ¿Cuántos alimentos tienen más de 0.1 mg de tiamina (vitamina B1)?
4. ¿Qué alimento tiene la mayor suma de vitaminas (vitamina A + tiamina + riboflavina + niacina + vitamina C)?
5. ¿Qué alimentos tienen más de 1 mg de hierro y menos de 3 g de grasas?

## Estructura del proyecto

```
.
├── Dataset.csv     # Datos de entrada (separados por comas)
├── mapper.py       # Fase Map: lee el CSV y emite pares clave-valor
├── reducer.py      # Fase Reduce: agrupa por clave y calcula los resultados
└── README.md
```

## Cómo funciona

**Mapper (`mapper.py`)**
Lee el CSV desde la entrada estándar, omite la cabecera y, por cada alimento, emite líneas con el formato `clave<TAB>valor`:

| Clave | Valor emitido                     | Pregunta |
|-------|-----------------------------------|----------|
| 1     | `alimento\|grasas`                | 1        |
| 2     | `alimento\|vitamina_c`            | 2        |
| 3     | `alimento\|tiamina`               | 3        |
| 4     | `alimento\|suma_vitaminas`        | 4        |
| 5     | `alimento\|hierro\|grasas`        | 5 (solo si hierro > 1 y grasas < 3) |

Los valores `-` o vacíos se tratan como `0`.

**Reducer (`reducer.py`)**
Recibe las líneas ordenadas, las agrupa por clave y calcula la respuesta de cada pregunta (máximos, conteo y filtrado).

## Requisitos

- Python 3.x

## Ejecución

### Linux / macOS / WSL / Git Bash

```bash
cat Dataset.csv | python3 mapper.py | sort | python3 reducer.py
```

### Windows (PowerShell)

```powershell
Get-Content Dataset.csv -Encoding UTF8 | python mapper.py | sort | python reducer.py
```

> Si `python` no funciona, prueba con `py`.
> Si las tildes se ven mal, ejecuta antes:
> `$OutputEncoding = [Console]::OutputEncoding = [Text.Encoding]::UTF8`

### Hadoop Streaming (opcional)

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files mapper.py,reducer.py \
  -mapper "python3 mapper.py" \
  -reducer "python3 reducer.py" \
  -input /ruta/Dataset.csv \
  -output /ruta/salida
```

El comando con `sort` simula la fase de *shuffle & sort* de MapReduce.

## Salida esperada

```
1	Alimento con mayor cantidad de grasas: <alimento> - <valor> gramos
2	Alimento con mayor cantidad de vitamina C: <alimento> - <valor> mg
3	Alimentos con más de 0.1 mg de tiamina: <cantidad>
4	Alimento con mayor suma de vitaminas: <alimento> - <valor>
5	Alimentos con más de 1 mg de hierro y menos de 3 g de grasas:
5	<alimento> - Hierro: <valor> mg - Grasas: <valor> g
...
```

## Notas

- La vitamina A está en unidades internacionales (UI) y las demás vitaminas en miligramos, por lo que en la pregunta 4 la vitamina A domina la suma. Se mantiene así según el enunciado del ejercicio.
- El dataset debe estar separado por comas y tener la cabecera en la primera línea.

## Autor

Tu nombre – Arquitectura, Seguimiento 2
