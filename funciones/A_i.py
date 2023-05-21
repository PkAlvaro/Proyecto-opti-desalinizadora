import pandas as pd


def a_i():
    df = pd.read_csv("datos/capacidad.csv", header=None, skiprows=1)
    datos_procesados = {}
    for indice, fila in df.iterrows():
        clave = fila[0]
        valor = int(fila[1])
        datos_procesados[clave] = valor
    return datos_procesados

if __name__ == "__main__":
    a = a_i()
    print(a)