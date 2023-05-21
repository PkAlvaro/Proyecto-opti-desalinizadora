import pandas as pd

def l_i():
    df = pd.read_csv("datos/costo_inversión.csv", header=None, skiprows=1)
    datos_procesados = {}
    for indice, fila in df.iterrows():
        clave = int(fila[0])
        valor = float(fila[1])
        datos_procesados[clave] = valor
    return datos_procesados

if __name__ == "__main__":
    a = l_i()
    print(a)