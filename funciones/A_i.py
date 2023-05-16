import csv

capacidad = []

with open("datos/A_i.csv", newline='') as A_i:
    lineas = csv.DictReader(A_i)
    for i in lineas:
        capacidad.append([int(i["Planta"]), int(i["Capacidad agua de mar"])])


ai = {i: capacidad[i - 1][1] for i in range(1, 24)}


