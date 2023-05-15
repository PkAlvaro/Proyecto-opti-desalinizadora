import csv

capacidad = []

with open("datos/MD_i.csv", newline='') as MD_i:
    lineas = csv.DictReader(MD_i)
    for i in lineas:
        capacidad.append([int(i["planta"]), float(i["cantidad de salmuera emitida (%)"].replace(',','.'))])

print(capacidad)