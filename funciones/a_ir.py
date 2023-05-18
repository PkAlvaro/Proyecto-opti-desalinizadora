import pandas as pd


def a_ir():
    df = pd.read_csv("datos/a_i,r.csv", header=None, skiprows=1)
    datos_procesados = {}
    for indice, fila in df.iterrows():
        clave = (fila[0], fila[1])
        valor = int(fila[2])
        datos_procesados[clave] = valor
    return datos_procesados