# def a_ir():
#     with open("datos/a_i,r.csv") as a_data:
#         a_data = a_data.readlines()[1:]
#         for i in range(len(a_data)):
#             a_data[i] = a_data[i].strip()
#             a_data[i] = a_data[i].split(',')
#         aux = []
#         print('\n')
#         a = 1
#         for linea in range(0, len(a_data), 15):
#             aux2 = list(filter(lambda x: x[0] == a_data[linea][0], a_data))
#             aux2 = list(map(lambda x: [int(x[1]), int(x[2])], aux2))
#             aux.append([False] + aux2)

#         a_data = [False] + aux

#     return a_data

# a_data = a_ir()
# air = {(i, r): a_data[i][r][1] for i in range(1, 24) for r in range(1, 16)}

import pandas as pd


def ar():
    df = pd.read_csv("datos/a_r.csv", header=None, skiprows=1)
    datos_procesados = {}
    for indice, fila in df.iterrows():
        clave = fila[0]
        valor = float(fila[1])
        datos_procesados[clave] = valor
    return datos_procesados

