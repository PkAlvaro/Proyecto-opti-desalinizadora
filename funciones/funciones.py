import pandas as pd

def sub_i(archivo):
    df = pd.read_csv(archivo, header=None, skiprows=1)
    datos_procesados = {}
    for indice, fila in df.iterrows():
        clave = fila[0]
        valor = float(fila[2])
        datos_procesados[clave] = valor
    return datos_procesados
