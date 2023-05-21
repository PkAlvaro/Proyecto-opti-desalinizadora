import pandas as pd

#pip install pandas
def mda_i():
    df = pd.read_csv("datos\MDA_i y MDN_i.csv", header=None, skiprows=1)
    cnt = {}
    for indice, fila in df.iterrows():
        clave = fila[0]
        valorcnt = int(fila[1])
        cnt[clave] = valorcnt
    return cnt


def mdn_i():
    df = pd.read_csv("datos\MDA_i y MDN_i.csv", header=None, skiprows=1)
    ca = {}
    for indice, fila in df.iterrows():
        clave = fila[0]
        valorca = float(fila[2])
        ca[clave] = valorca
    return ca

if __name__ == "__main__":
    a = mdn_i()
    print(a)