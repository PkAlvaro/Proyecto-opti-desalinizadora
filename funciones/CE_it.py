import pandas as pd


def ce_it():
    df = pd.read_csv("datos/costo_energía.csv", header=None, skiprows=1)
    cnt = {}
    for indice, fila in df.iterrows():
        clave = (int(fila[0]), int(fila[1]))
        valorcnt = float(fila[2])
        cnt[clave] = valorcnt
    return cnt
if __name__ == "__main__":
    a = ce_it()
    print(a)
