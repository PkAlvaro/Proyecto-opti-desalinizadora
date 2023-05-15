import csv

costo = []

with open("datos/L_i.csv", newline='') as L_i:
    lineas = csv.DictReader(L_i)
    for i in lineas:
        costo.append([int(i["Planta"]), int(i["Costo Inversion"])])

print(costo)