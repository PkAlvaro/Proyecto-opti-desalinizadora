import pandas as pd

def cnt():
    df = pd.read_csv("datos\CNT_i,t y CA_i,t.csv", header=None, skiprows=1)
    cnt = {}
    for indice, fila in df.iterrows():
        clave = (fila[0], fila[1])
        valorcnt = float(fila[2].replace(',', '.'))
        cnt[clave] = valorcnt
    return cnt

def ca():
    df = pd.read_csv("datos\CNT_i,t y CA_i,t.csv", header=None, skiprows=1)
    ca = {}
    for indice, fila in df.iterrows():
        clave = (fila[0], fila[1])
        valorca = float(fila[3].replace(',', '.'))
        ca[clave] = valorca
    return ca

if __name__ == "__main__":
    w = cnt()
    y = ca()
    print(w)
    print(y)