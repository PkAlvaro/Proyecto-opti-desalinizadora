import csv
def CTA_it():
    with open("datos/CTA_i,t.csv") as a_data:
        aux3 = []
        lineas = csv.DictReader(a_data)
        for i in lineas:
            aux3.append([int(i["Planta"]), int(i["Tiempo"]), float(i["Costo Transporte Agua de Mar a Planta"].replace(',','.'))])


        aux = []
        a = 1
        for linea in range(0, len(aux3), 20):
            aux2 = list(filter(lambda x: x[0] == aux3[linea][0], aux3))
            aux2 = list(map(lambda x: [int(x[1]), float(x[2])], aux2))
            aux.append([False] + aux2)

        aux3 = [False] + aux

    return aux3

a_data = CTA_it()
cta = {(i, t): a_data[i][t][1] for i in range(1, 24) for t in range(1, 20 + 1)}