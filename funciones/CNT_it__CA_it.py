import pandas as pd

#pip install pandas
def cnt():
    df = pd.read_csv("datos/costos_agua.csv", header=None, skiprows=1)
    cnt = {}
    for indice, fila in df.iterrows():
        clave = (fila[0], fila[1])
        valorcnt = float(fila[2])
        cnt[clave] = valorcnt
    return cnt


def ca():
    df = pd.read_csv("datos/costos_agua.csv", header=None, skiprows=1)
    ca = {}
    for indice, fila in df.iterrows():
        clave = (fila[0], fila[1])
        valorca = float(fila[3])
        ca[clave] = valorca
    return ca