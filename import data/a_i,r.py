import csv

def a_ir():
    archivo = open("datos/a_i,r.csv")
    a_data = archivo.readlines()[1:]
    archivo.close()
    print(a_data)
    
print(a_ir())