import pandas as pd

def capi_r():
    df = pd.read_csv("datos/CAPI_r.csv", header=None, skiprows=1)
    datos_procesados = {}
    for indice, fila in df.iterrows():
        clave = fila[0]
        valor = float(fila[1])
        datos_procesados[clave] = valor
    return datos_procesados

# import csv

# capacidad = []

# with open("datos/CAPI_r.csv", newline='') as CAPI_r:
#     lineas = csv.DictReader(CAPI_r)
#     for i in lineas:
#         capacidad.append([int(i["Region"]), int(i["Capacidad maxima en el inventario (m3)"])])

# capi = {r: capacidad[r - 1][1] for r in range(1, 16)}
