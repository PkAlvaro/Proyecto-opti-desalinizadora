import pandas as pd

def m_it():
    df = pd.read_csv("datos/costo_mantenimiento.csv", header=None, skiprows=1)
    cnt = {}
    for indice, fila in df.iterrows():
        clave = (int(fila[0]), int(fila[1]))
        valorcnt = float(fila[2])
        cnt[clave] = valorcnt
    return cnt

if __name__ == "__main__":
    a = m_it()
    print(a)