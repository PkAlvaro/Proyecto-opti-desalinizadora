import csv

costo = []

with open("datos/CI_t.csv", newline='') as CI_t:
    lineas = csv.DictReader(CI_t)
    for i in lineas:
        costo.append([int(i["Planta"]), float(i["Costo Inversion"].replace(',','.'))])

print(costo)