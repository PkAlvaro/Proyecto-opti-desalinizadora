import csv

costo = []

with open("datos/CI_t.csv", newline='') as CI_t:
    lineas = csv.DictReader(CI_t)
    for i in lineas:
        costo.append([int(i["Tiempo"]), float(i["Costo Almacenar Agua (MMUS /mm3)"].replace(',','.'))])


ci = {t: costo[t - 1][1] for t in range(1, 21)}