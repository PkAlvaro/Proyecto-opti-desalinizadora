import pandas as pd

# import csv

# capacidad1 = []
# capacidad2 = []

# with open("datos/DD_i y DF_i.csv", newline='', encoding='utf-8') as DD_q:
#     lineas = csv.DictReader(DD_q)
#     for i in lineas:
#         capacidad1.append([str(i["Planta"]), float(i["limite de salinidad dentro de la ZPL (kilos/m3)"])])
#         capacidad2.append([str(i["Planta"]), float(i["limite de salinidad fuera de la ZPL (kilos/m3)"])])

# # ddq = {q: capacidad1[q - 1][1] for q in range(1, 16)}
# # ddf = {q: capacidad2[q - 1][1] for q in range(1, 16)}

def dd_i():
    df = pd.read_csv("datos/DD_i y DF_i.csv", header=None, skiprows=1)
    datos_procesados = {}
    for indice, fila in df.iterrows():
        clave = int(fila[0])
        valor = float(fila[1])
        datos_procesados[clave] = valor
    return datos_procesados

def df_i():
    df = pd.read_csv("datos/DD_i y DF_i.csv", header=None, skiprows=1)
    datos_procesados = {}
    for indice, fila in df.iterrows():
        clave = int(fila[0])
        valor = float(fila[2])
        datos_procesados[clave] = valor
    return datos_procesados