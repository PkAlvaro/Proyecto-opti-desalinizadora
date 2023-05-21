import pandas as pd


def dd_i():
    df = pd.read_csv("datos/rango_eliminacion.csv", header=None, skiprows=1)
    datos_procesados = {}
    for indice, fila in df.iterrows():
        clave = int(fila[0])
        valor = float(fila[1])
        datos_procesados[clave] = valor
    return datos_procesados

def df_i():
    df = pd.read_csv("datos/rango_eliminacion.csv", header=None, skiprows=1)
    datos_procesados = {}
    for indice, fila in df.iterrows():
        clave = int(fila[0])
        valor = float(fila[2])
        datos_procesados[clave] = valor
    return datos_procesados