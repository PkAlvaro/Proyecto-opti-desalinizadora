import pandas as pd


def ar():
    df = pd.read_csv("datos/existencia.csv", header=None, skiprows=1)
    datos_procesados = {}
    for indice, fila in df.iterrows():
        clave = fila[0]
        valor = float(fila[1])
        datos_procesados[clave] = valor
    return datos_procesados

