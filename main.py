from gurobipy import GRB
import gurobipy as gp
from gurobipy import quicksum
from random import randint, uniform, seed
from funciones import a_ir ,a_r, A_i, ACU_it, CAPI_r, CD_iq__CF_iq, CE_it, CF_it, CI_t, CNT_it__CA_it, CTA_it, D_rt, DD_q__DF_q, EC_ir, L_i, M_it, MD_i, W_it

# seed(8)

#Definicion de conjuntos#

Plantas = range(1, 24)
Tiempo = range(1, 21)
Region = range(1, 16)

#Parametros

#Parametros rel. con agua desalinizada y plantas

air = a_ir.a_ir()
a = a_r.ar()
aux = {(i,r): randint(0,1) for i in Plantas for r in Region}

#cnt = CNT_it__CA_it.cnt()
#ca = CNT_it__CA_it.ca()
cnt = {(i,t): uniform(0.00000009, 0.00000002) for i in Plantas for t in Tiempo}
ca = {(i,t): uniform(0.000001, 0.000002) for i in Plantas for t in Tiempo}

d = D_rt.d_rt()
# print('\n', d)
#l = L_i.li
l = {i: uniform(2, 3) for i in Plantas}

m = M_it.m_it()
cta = CTA_it.cta_it()
cf = CF_it.cf
aa = A_i.a_i()
cam = 3000

#Parametros relacionados con energia

ce = CE_it.ce_it()
gem = 1063194000
w = W_it.w_it()

#Parametros relacionados con ruido y zona urbana

RP = 125
ec = EC_ir.ec
acu = ACU_it.acu

#Parametros relacionados con la contaminacion de salmuera

# dd = DD_q__DF_q.ddq
# df = DD_q__DF_q.ddf
#dd = {q: randint(500000, 900000) for q in Metales} #no hay metales
#df = {q: randint(400000, 900000) for q in Metales} #no hay metales
# cdz = CD_iq__CF_iq.cdz
# cfz = CD_iq__CF_iq.cfz
cdz = {i: uniform(0.00000024, 0.00000040) for i in Plantas}
cfz = {i: uniform(0.00000048, 0.00000080) for i in Plantas}
md = MD_i.md
#mda =
#mdn = 

#Parametros relacionados con el inventario

cii = CI_t.ci_t()
capi = CAPI_r.capi_r()
M = 10**10


model = gp.Model()
model.setParam("TimeLimit", 300)

#VARIABLES DEL MODELO.

x = model.addVars(Plantas, Tiempo, vtype = GRB.CONTINUOUS, name = "x_it")
h = model.addVars(Plantas, Tiempo, vtype = GRB.CONTINUOUS, name = "h_it")
y = model.addVars(Plantas, Tiempo, vtype = GRB.CONTINUOUS, name = "y_it")
ii = model.addVars(Region, Tiempo, vtype = GRB.CONTINUOUS, name = "I_rt")
z = model.addVars(Plantas, vtype = GRB.BINARY, name = "z_i")
zpl = model.addVars(Plantas, vtype = GRB.BINARY, name = "zpl_i")

#################
#ar = #muestra si la region r tiene planta 





##################
model.update()

#RESTRICCIONES

model.addConstrs((quicksum((x[i,t] + h[i,t]) * air[i,r] for i in Plantas) >= d[r,t] * a[r] for t in Tiempo for r in Region), name = "R1" )

#model.addConstrs(((acu[i,t] * (x[i,t] + h[i,t]) * ec[i,r])/(365 * 365) <= 500000 for i in Plantas for t in Tiempo for r in Region), name = "R2" ) 

#model.addConstrs((md[i] * (x[i,t] + h[i,t]) <= (zpl[i] * dd[q]) + df[q] * (1 - zpl[i]) for i in Plantas for t in Tiempo for q in Metales), name = "R3" )

model.addConstrs((quicksum((x[i,t] + h[i,t]) * w[i,t] for i in Plantas) <= gem for t in Tiempo), name = "R4" )

#model.addConstrs((y[i,t] <= cam for i in Plantas for t in Tiempo), name = "R5.1")
#model.addConstrs((y[i,t] <= aa[i] for i in Plantas for t in Tiempo), name = "R5.2")

#model.addConstrs((0.6 * y[i,t] >= x[i,t] for i in Plantas for t in Tiempo), name = "R6.1")
#model.addConstrs((0.8 * y[i,t] >= h[i,t] for i in Plantas for t in Tiempo), name = "R6.2")

#model.addConstrs((h[i,t] <= M * z[i] for i in Plantas for t in Tiempo), name = "R7.1")
#model.addConstrs( (x[i,t] <= M * (1 - z[i]) for i in Plantas for t in Tiempo), name = "R7.2")

#model.addConstrs((ii[r,t] == ii[r,t-1] + quicksum((x[i,t] + h[i,t])* air[i,r] for i in Plantas) - d[r,t]*a[r] for t in range(2, 20 + 1) for r in Region), name = "R8.1")

#model.addConstrs((ii[r,1] == 0 + quicksum( (x[i,1] + h[i,1]) * air[i,r] for i in Plantas) - d[r,1]*a[r] for r in Region), name = "R8.2")

#model.addConstrs((ii[r,t] <= capi[r] for r in Region if r != 13 and r!= 14 for t in Tiempo), name = "R9")


# #FUNCION OBJETIVO

# objetivo = quicksum ( l[i] * z[i] + quicksum(h[i,t] * cnt[i,t] + m[i,t] * (x[i,t] + h[i,t]) + ca[i,t] * x[i,t] + cta[i,t] * y[i,t] + ce[i,t] * w[i,t] * (x[i,t] + h[i,t]) + cf[i,t] for t in Tiempo) for i in Plantas) + quicksum(i[r,t] * cii[t] for t in Tiempo for r in Region) + quicksum(zpl[i]*cdz[i,q] + (1 - zpl[i])*cfz[i,q] for i in Plantas for q in Metales)

objetivo = quicksum( l[i] * z[i] + zpl[i]*cdz[i] + (1 - zpl[i])*cfz[i] + quicksum(h[i,t] * cnt[i,t] + m[i,t] * (x[i,t] + h[i,t]) + ca[i,t] * x[i,t] + cta[i,t] * y[i,t] + ce[i,t] * (x[i,t] + h[i,t]) + cf[i,t] for t in Tiempo) for i in Plantas) + quicksum(ii[r, t] * cii[t] for t in Tiempo for r in Region)

model.setObjective(objetivo, GRB.MINIMIZE)

#OPTIMIZA

model.optimize()

#ATRIBUTOS
model.printAttr("X")

#model.printAttr("X")