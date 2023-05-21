import pandas as pd


def ci_t():
    df = pd.read_csv("datos/costo_almacenamiento.csv", header=None, skiprows=1)
    datos_procesados = {}
    for indice, fila in df.iterrows():
        clave = fila[0]
        valor = float(fila[1])
        datos_procesados[clave] = valor
    return datos_procesados