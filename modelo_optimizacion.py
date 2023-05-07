from gurobipy import GRB
import gurobipy as gp
from gurobipy import quicksum
from random import randint, uniform

print('p')

#Definicion de conjuntos#
Plantas = range(23)
Tiempo = range(20)
Region = range(16)
Metales = range(8)

#Parametros

#Parametros rel. con agua desalinizada y plantas
a = {(i,r): randint(0,1) for i in Plantas for r in Region}

#a = {(0, 0): 1, (0, 1): 0, (0, 2): 0, (0, 3): 0, (0, 4): 0, (1, 0): 0, (1, 1): 1, (1, 2): 0, (1, 3): 0, (1, 4): 0, (2, 0): 0, (2, 1): 0, (2, 2): 1, (2, 3): 0, (2, 4): 0, (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 1, (3, 4): 0, (4, 0): 0, (4, 1): 0, (4, 2): 0, (4, 3): 0, (4, 4): 1}

#a = {(0, 0): 1, (0, 1): 0, (1, 0): 0, (1, 1): 1}
cnt = {(i,t): randint(80, 200) for i in Plantas for t in Tiempo}
ca = {(i,t): randint(120, 180) for i in Plantas for t in Tiempo}
d = {(r,t): randint(12500, 20000) for r in Region for t in Tiempo}
l = {i: randint(3000000, 5000000) for i in Plantas}
m = {(i,t): randint(40, 100) for i in Plantas for t in Tiempo}
cta = {(i,t): randint(20, 50) for i in Plantas for t in Tiempo}
ctr = {(i,t): randint(20, 40) for i in Plantas for t in Tiempo}
cf = {(i,t): randint(5, 10) for i in Plantas for t in Tiempo}
aa = {i: randint(1500000, 3000000) for i in Plantas}
cam = 10**7

#Parametros relacionados con energia
ce = {(i,t): randint(5, 10) for i in Plantas for t in Tiempo}
gem = 10**7
w = {(i,t): uniform(0.0005, 0.001) for i in Plantas for t in Tiempo}

#Parametros relacionados con ruido y zona urbana

RP = 125*365
ec = {(i,r): randint(0,1) for i in Plantas for r in Region}
acu = {(i,t): uniform(0.000033,0.00005) for t in Tiempo for i in Plantas}

#Parametros relacionados con la contaminacion quimica

dd = {q: randint(20, 60) for q in Metales}
df = {q: randint(40, 80) for q in Metales}
md = {(i,q,t): uniform(0.00002, 0.00006) for i in Plantas for q in Metales for t in Tiempo}

#Parametros relacionados con el inventario

cii = {t: uniform(0.05, 0.1) for t in Tiempo}
capi = {r: uniform(30000000, 500000000) for r in Region}
M = 10**7

#Parametros zpl

cd = {(i,q): randint(500, 800) for i in Plantas for q in Metales}
cff = {(i,q): randint(600, 800) for i in Plantas for q in Metales}




model = gp.Model()
model.setParam("TimeLimit", 300)

#VARIABLES DEL MODELO.

x = model.addVars(Plantas, Tiempo, vtype = GRB.CONTINUOUS, name = "x_it")
h = model.addVars(Plantas, Tiempo, vtype = GRB.CONTINUOUS, name = "h_it")
y = model.addVars(Plantas, Tiempo, vtype = GRB.CONTINUOUS, name = "y_it")
i = model.addVars(Region, Tiempo, vtype = GRB.CONTINUOUS, name = "I_rt")
z = model.addVars(Plantas, vtype = GRB.BINARY, name = "z_i")
zpl = model.addVars(Plantas, vtype = GRB.BINARY, name = "zpl_i")


model.update()

#RESTRICCIONES

model.addConstrs((quicksum((x[i,t] + h[i,t]) * a[i,r] for i in Plantas) >= d[r,t] for t in Tiempo for r in Region), name = "R1" )

model.addConstrs((acu[i,t] * (x[i,t] + h[i,t]) * ec[i,r] <= RP for i in Plantas for t in Tiempo for r in Region), name = "R2" ) 

model.addConstrs((md[i,q,t] * (x[i,t] + h[i,t]) <= (zpl[i] * dd[q]) + df[q] * (1 - zpl[i]) for i in Plantas for t in Tiempo for q in Metales), name = "R3" )

model.addConstrs(((x[i,t] + h[i,t]) * w[i,t] <= gem for i in Plantas for t in Tiempo), name = "R4" )

model.addConstrs((y[i,t] <= cam for i in Plantas for t in Tiempo), name = "R5.1")
model.addConstrs((y[i,t] <= aa[i] for i in Plantas for t in Tiempo), name = "R5.2")

model.addConstrs((y[i,t] >= 0.6 * x[i,t] for i in Plantas for t in Tiempo), name = "R6.1")
model.addConstrs((y[i,t] >= 0.8 * h[i,t] for i in Plantas for t in Tiempo), name = "R6.2")

model.addConstrs((h[i,t] <= M * z[i] for i in Plantas for t in Tiempo),name = "R7.1")
model.addConstrs( (x[i,t] <= M * (1 - z[i]) for i in Plantas for t in Tiempo) , name = "R7.2")


model.addConstrs((i[r,t] == i[r,t-1] + quicksum((x[i,t] + h[i,t]) * a[i,r] for i in Plantas) for t in range(2, len(Tiempo) + 1 ) for r in Region), name = "R8.1")
model.addConstrs((i[r,1] == 0 + quicksum((x[i,1] + h[i,1]) * a[i,r] for i in Plantas) for r in Region), name = "R8.2")

model.addConstrs((i[r,t] <= capi[r] for r in Region for t in Tiempo), name = "R9")


#FUNCION OBJETIVO

objetivo = quicksum ( l[i] * z[i] + quicksum(h[i,t] * cnt[i,t] + m[i,t] * (x[i,t] + h[i,t]) + ca[i,t] * x[i,t] + cta[i,t] * y[i,t] + ce[i,t] * w[i,t] * (x[i,t] + h[i,t]) + cf[i,t] for t in Tiempo) for i in Plantas) + quicksum(i[r,t] * cii[t] for t in Tiempo for r in Region) + quicksum(zpl[i]*cd[i,q] + (1 - zpl[i])*cff[i,q] for i in Plantas for q in Metales)
model.setObjective(objetivo, GRB.MINIMIZE)



#OPTIMIZA

model.optimize()

#ATRIBUTOS
#model.printAttr("X")

#model.printAttr("X")

