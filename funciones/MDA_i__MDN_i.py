import pandas as pd

def mda_i():
    df = pd.read_csv("datos/proporcion_desechado.csv", header=None, skiprows=1, sep=';')
    cnt = {}
    for indice, fila in df.iterrows():
        clave = int(fila[0])
        valorcnt = float(fila[1].replace(',', '.'))
        cnt[clave] = valorcnt
    return cnt


def mdn_i():
    df = pd.read_csv("datos/proporcion_desechado.csv", header=None, skiprows=1, sep= ';')
    ca = {}
    for indice, fila in df.iterrows():
        clave = int(fila[0])
        valorca = float(fila[2].replace(',', '.'))
        ca[clave] = valorca
    return ca

if __name__ == "__main__":
    a = mdn_i()
    b = mda_i()
    print(b)