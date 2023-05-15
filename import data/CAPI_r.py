
import csv

capacidad = []

with open("datos/CAPI_r.csv", newline='') as CAPI_r:
    lineas = csv.DictReader(CAPI_r)
    for i in lineas:
        capacidad.append([int(i["Region"]), int(i["Capacidad maxima en el inventario (mm3)"])])


print(capacidad)