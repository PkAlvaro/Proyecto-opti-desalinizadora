
import csv

capacidad = []

with open("datos/DD_q y DF_q.csv", newline='', encoding='utf-8') as DD_q:
    lineas = csv.DictReader(DD_q)
    for i in lineas:
        capacidad.append([str(i["Metal pesado"]), float(i["Dentro de la ZPL (mg/mm3)"].replace(',','.')), float(i["Fuera de la ZPL (mg/mm3)"].replace(',','.'))])

print(capacidad)