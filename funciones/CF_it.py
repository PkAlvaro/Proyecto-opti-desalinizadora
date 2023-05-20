def cf_it():
    with open("datos/CF_i,t.csv") as a_data:
        a_data = a_data.readlines()[1:]
        for i in range(len(a_data)):
            a_data[i] = a_data[i].strip()
            a_data[i] = a_data[i].split(',')
        aux = []
        print('\n')
        a = 1
        for linea in range(0, len(a_data), 20):
            aux2 = list(filter(lambda x: x[0] == a_data[linea][0], a_data))
            aux2 = list(map(lambda x: [int(x[1]), float(x[2])], aux2))
            aux.append([False] + aux2)

        a_data = [False] + aux

    return a_data

a_data = cf_it()
cf = {(i, t): a_data[i][t][1] for i in range(1, 24) for t in range(1, 21)}
