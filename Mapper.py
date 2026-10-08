import sys
import csv

def convertir(valor):
    valor = valor.strip()
    if valor in ("-", ""):
        return 0.0
    return float(valor.replace(",", "."))

entrada = (l for l in sys.stdin)
lector = csv.reader(entrada)   # delimitador: coma
next(lector)                   # saltar cabecera

for f in lector:
    if len(f) < 11:
        continue

    alimento    = f[0].strip()
    grasas      = convertir(f[3])
    hierro      = convertir(f[5])
    vitamina_a  = convertir(f[6])
    tiamina     = convertir(f[7])
    riboflavina = convertir(f[8])
    niacina     = convertir(f[9])
    vitamina_c  = convertir(f[10])

    print(f"1\t{alimento}|{grasas}")
    print(f"2\t{alimento}|{vitamina_c}")
    print(f"3\t{alimento}|{tiamina}")

    suma = vitamina_a + tiamina + riboflavina + niacina + vitamina_c
    print(f"4\t{alimento}|{suma}")

    if hierro > 1 and grasas < 3:
        print(f"5\t{alimento}|{hierro}|{grasas}")