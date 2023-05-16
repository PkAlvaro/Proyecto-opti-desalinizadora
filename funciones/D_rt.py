import pandas as pd


def d_rt():
    df = pd.read_csv("datos/D_r,t.csv", header=None, skiprows=1)
    datos_procesados = {}
    for indice, fila in df.iterrows():
        clave = (fila[1], fila[0])
        valor = int(fila[2])
        datos_procesados[clave] = valor
    return datos_procesados


if __name__ == "__main__":
    w = d_rt()