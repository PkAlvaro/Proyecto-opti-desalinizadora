import csv

capacidad = []

with open("datos/A_i.csv", newline='') as A_i:
    lineas = csv.DictReader(A_i)
    for i in lineas:
        capacidad.append([int(i["Planta"]), int(i["Capacidad agua de mar"])])



print(capacidad)


