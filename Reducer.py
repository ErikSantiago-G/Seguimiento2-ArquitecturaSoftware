import sys

datos = {"1": [], "2": [], "3": [], "4": [], "5": []}

for linea in sys.stdin:
    linea = linea.strip()
    if not linea:
        continue
    clave, valor = linea.split("\t", 1)
    datos[clave].append(valor.split("|"))

# 1: mayor grasa
a, g = max(((p[0], float(p[1])) for p in datos["1"]), key=lambda x: x[1])
print(f"1\tAlimento con mayor cantidad de grasas: {a} - {g} gramos")

# 2: mayor vitamina C
a, v = max(((p[0], float(p[1])) for p in datos["2"]), key=lambda x: x[1])
print(f"2\tAlimento con mayor cantidad de vitamina C: {a} - {v} mg")

# 3: cuántos con tiamina > 0.1
n = sum(1 for p in datos["3"] if float(p[1]) > 0.1)
print(f"3\tAlimentos con más de 0.1 mg de tiamina: {n}")

# 4: mayor suma de vitaminas
a, s = max(((p[0], float(p[1])) for p in datos["4"]), key=lambda x: x[1])
print(f"4\tAlimento con mayor suma de vitaminas: {a} - {round(s, 2)}")

# 5: hierro > 1 y grasas < 3
print("5\tAlimentos con más de 1 mg de hierro y menos de 3 g de grasas:")
for p in datos["5"]:
    print(f"5\t{p[0]} - Hierro: {p[1]} mg - Grasas: {p[2]} g")