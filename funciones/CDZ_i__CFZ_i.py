import pandas as pd


def cdz_i():
    df = pd.read_csv("datos\costo_eliminacion.csv", header=None, skiprows=1, sep=';')
    cnt = {}
    for indice, fila in df.iterrows():
        clave = fila[0]
        valorcnt = float(fila[1].replace(',', '.'))
        cnt[clave] = valorcnt
    return cnt

def cfz_i():
    df = pd.read_csv("datos\costo_eliminacion.csv", header=None, skiprows=1, sep=';')
    ca = {}
    for indice, fila in df.iterrows():
        clave = fila[0]
        valorca = float(fila[2].replace(',', '.'))
        ca[clave] = valorca
    return ca

if __name__ == "__main__":
    a = cfz_i2()
    b = cdz_i2()
    print(a,b)