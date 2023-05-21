# import csv

# capacidad1 = []
# capacidad2= []

# with open("datos/CD_i,q y CF_iq.csv", newline='') as CDyCF_iq:
#     lineas = csv.DictReader(CDyCF_iq)
#     for i in lineas:
#         capacidad1.append([int(i["Planta"]), int(i["Metal pesado"]), float(i["Costo dentro ZPL"].replace(',','.'))])
#         capacidad2.append([int(i["Planta"]), int(i["Metal pesado"]), float(i["Costo Fuera ZPL"].replace(',','.'))])
#     aux = []
#     auxl2 = []

#     for linea in range(0, len(capacidad1), 15):
#         aux2 = list(filter(lambda x: x[0] == capacidad1[linea][0], capacidad1))
#         aux2 = list(map(lambda x: [int(x[1]), float(x[2])], aux2))
#         aux.append([False] + aux2)

#     for linea in range(0, len(capacidad1), 15):
#         aux3 = list(filter(lambda x: x[0] == capacidad2[linea][0], capacidad2))
#         aux3 = list(map(lambda x: [int(x[1]), float(x[2])], aux3))
#         auxl2.append([False] + aux3)
#     dentro = [False] + aux
#     fuera = [False] + auxl2


# cdz = {(i, q): dentro[i][q][1] for i in range(1, 24) for q in range(1, 15 + 1)}
# cfz = {(i, q): fuera[i][q][1] for i in range(1, 24) for q in range(1, 15 + 1)}


import pandas as pd

#pip install pandas
def cdz_i():
    df = pd.read_csv("datos\CDZ_i y CFZ_i.csv", header=None, skiprows=1)
    cnt = {}
    for indice, fila in df.iterrows():
        clave = fila[0]
        valorcnt = float(fila[1])
        cnt[clave] = valorcnt
    return cnt


def cfz_i():
    df = pd.read_csv("datos\CDZ_i y CFZ_i.csv", header=None, skiprows=1)
    ca = {}
    for indice, fila in df.iterrows():
        clave = fila[0]
        valorca = float(fila[2])
        ca[clave] = valorca
    return ca