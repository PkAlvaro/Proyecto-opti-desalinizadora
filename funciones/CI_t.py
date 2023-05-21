import pandas as pd
# import csv

# costo = []

# with open("datos/CI_t.csv", newline='') as CI_t:
#     lineas = csv.DictReader(CI_t)
#     for i in lineas:
#         costo.append([int(i["Tiempo"]), float(i["Costo Almacenar Agua (MMUS /mm3)"])])


# ci = {t: costo[t - 1][1] for t in range(1, 21)}

def ci_t():
    df = pd.read_csv("datos/CI_t.csv", header=None, skiprows=1)
    datos_procesados = {}
    for indice, fila in df.iterrows():
        clave = fila[0]
        valor = float(fila[1])
        datos_procesados[clave] = valor
    return datos_procesados