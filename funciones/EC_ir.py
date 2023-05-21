
def EC_ir():
    with open("datos/zona_urbana.csv") as a_data:
        a_data = a_data.readlines()[1:]
        for i in range(len(a_data)):
            a_data[i] = a_data[i].strip()
            a_data[i] = a_data[i].split(',')
        aux = []
        print('\n')
        a = 1
        for linea in range(0, len(a_data), 15):
            aux2 = list(filter(lambda x: x[0] == a_data[linea][0], a_data))
            aux2 = list(map(lambda x: [float(x[1]), float(x[2])], aux2))
            aux.append([False] + aux2)

        a_data = [False] + aux

    return a_data

a_data = EC_ir()
ec = {(i, r): a_data[i][r][1] for i in range(1, 24) for r in range(1, 16)}

