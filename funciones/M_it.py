import csv

def m_it():
    with open("datos/M_i,t.csv", newline='') as a_data:
        aux3 = []
        lineas = csv.DictReader(a_data)
        for j in lineas:
            aux3.append([int(j["Planta"]), int(j["Tiempo"]), float(j["Coste de Mantenimiento"].replace(',', '.'))])

        aux = []
        for linea in range(0, len(aux3), 15):
            aux2 = list(filter(lambda x: x[0] == aux3[linea][0], aux3))
            aux2 = list(map(lambda x: [int(x[1]), float(x[2])], aux2))
            aux.append([False] + aux2)

        aux3 = [False] + aux

    return aux3


data = m_it()
mit = {(i, t): data[i][t][1] for i in range(1, 24) for t in range(1, 20 + 1)}