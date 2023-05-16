import csv

capacidad = []

with open("datos/MD_i.csv", newline='') as MD_i:
    lineas = csv.DictReader(MD_i)
    for i in lineas:
        capacidad.append([int(i["planta"]), float(i["cantidad de salmuera emitida (%)"].replace(',','.'))])

md = {i: capacidad[i - 1][1] for i in range(1, 24)}