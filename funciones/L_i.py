import pandas as pd

# import csv

# costo = []

# with open("datos/L_i.csv", newline='') as L_i:
#     lineas = csv.DictReader(L_i)
#     for i in lineas:
#         costo.append([int(i["Planta"]), float(i["Costo Inversion (USD)"])])

# li = {i: costo[i - 1][1] for i in range(1, 24)}

def l_i():
    df = pd.read_csv("datos/L_i.csv", header=None, skiprows=1)
    datos_procesados = {}
    for indice, fila in df.iterrows():
        clave = fila[0]
        valor = int(fila[1])
        datos_procesados[clave] = valor
    return datos_procesados