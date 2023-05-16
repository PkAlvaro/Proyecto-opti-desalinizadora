
import csv

capacidad1 = []
capacidad2 = []

with open("datos/DD_q y DF_q.csv", newline='', encoding='utf-8') as DD_q:
    lineas = csv.DictReader(DD_q)
    for i in lineas:
        capacidad1.append([str(i["Metal pesado"]), float(i["Dentro de la ZPL (mg/mm3)"].replace(',','.'))])
        capacidad2.append([str(i["Metal pesado"]), float(i["Fuera de la ZPL (mg/mm3)"].replace(',','.'))])
    

ddq = {q: capacidad1[q - 1][1] for q in range(1, 16)}
ddf = {q: capacidad2[q - 1][1] for q in range(1, 16)}