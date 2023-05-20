import csv
import pandas as pd

# capacidad = []

# with open("datos/A_i.csv", newline='') as A_i:
#     lineas = csv.DictReader(A_i)
#     for i in lineas:
#         capacidad.append([int(i["Planta"]), int(i["Capacidad_agua_de_mar"])])

# ai = {i: capacidad[i - 1][1] for i in range(1, 24)}



def a_i():
    df = pd.read_csv("datos/A_i.csv", header=None, skiprows=1)
    datos_procesados = {}
    for indice, fila in df.iterrows():
        clave = fila[0]
        valor = int(fila[1])
        datos_procesados[clave] = valor
    return datos_procesados