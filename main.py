from gurobipy import GRB
import gurobipy as gp
from gurobipy import quicksum
from funciones import CDZ_i__CFZ_i, MDA_i__MDN_i, a_ir ,a_r, A_i, ACU_it, CAPI_r, CE_it, CF_it, CI_t, CNT_it__CA_it, CTA_it, D_rt, DD_i__DF_i, EC_ir, L_i, M_it, W_it

# Definicion de conjuntos#

Plantas = range(1, 24)
Tiempo = range(1, 21)
Region = range(1, 16)

# Parametros

#################################################
# Parametros rel. con agua desalinizada y plantas #
#################################################

air = a_ir.a_ir()
a = a_r.ar()
cnt = CNT_it__CA_it.cnt()
ca = CNT_it__CA_it.ca()
d = D_rt.d_rt()
l = L_i.l_i()
m = M_it.m_it()
cta = CTA_it.cta_it()
cf = CF_it.cf
aa = A_i.a_i()
cam = 4000 * 365

#####################################
#Parametros relacionados con energia#
#####################################

ce = CE_it.ce_it()
gem = 1063194000
w = W_it.w_it()

#################################################
# Parametros relacionados con ruido y zona urbana#
#################################################

RP = 125
ec = EC_ir.ec
acu = ACU_it.acu

##########################################################
# Parametros relacionados con la contaminacion de salmuera#
##########################################################


dd = DD_i__DF_i.dd_i()
df = DD_i__DF_i.df_i()
cdz = CDZ_i__CFZ_i.cdz_i()
cfz = CDZ_i__CFZ_i.cfz_i()
mda = MDA_i__MDN_i.mda_i()
mdn = MDA_i__MDN_i.mdn_i()


##############################################
# Parametros relacionados con el inventario #
##############################################

cii = CI_t.ci_t()
capi = CAPI_r.capi_r()
M = 10**10

##########################################################
# Generación del modelo #
##########################################################

model = gp.Model()
model.setParam("TimeLimit", 300)

# VARIABLES DEL MODELO.

x = model.addVars(Plantas, Tiempo, vtype = GRB.CONTINUOUS, name = "x_it")
h = model.addVars(Plantas, Tiempo, vtype = GRB.CONTINUOUS, name = "h_it")
y = model.addVars(Plantas, Tiempo, vtype = GRB.CONTINUOUS, name = "y_it")
ii = model.addVars(Region, Tiempo, vtype = GRB.CONTINUOUS, name = "I_rt")
z = model.addVars(Plantas, vtype = GRB.BINARY, name = "z_i")
zpl = model.addVars(Plantas, vtype = GRB.BINARY, name = "zpl_i")

##################
model.update()

#RESTRICCIONES

model.addConstrs(((acu[i,t] * (x[i,t] + h[i,t]) * ec[i,r])/(365) <= RP for i in Plantas for t in Tiempo for r in Region), name = "R2" ) 

model.addConstrs((mda[i] * x[i,t] + mdn[i] * h[i,t] <= ((zpl[i] * dd[i]) + df[i] * (1 - zpl[i])) * cam for i in Plantas for t in Tiempo for i in Plantas), name = "R3" )

model.addConstrs((quicksum((x[i,t] + h[i,t]) * w[i,t] for i in Plantas) <= gem for t in Tiempo), name = "R4" )

model.addConstrs((y[i,t] <= cam for i in Plantas for t in Tiempo), name = "R5.1")
model.addConstrs((y[i,t] <= aa[i] for i in Plantas for t in Tiempo), name = "R5.2")

model.addConstrs((0.6 * y[i,t] >= x[i,t] for i in Plantas for t in Tiempo), name = "R6.1")
model.addConstrs((0.8 * y[i,t] >= h[i,t] for i in Plantas for t in Tiempo), name = "R6.2")

model.addConstrs((h[i,t] <= M * z[i] for i in Plantas for t in Tiempo), name = "R7.1")
model.addConstrs( (x[i,t] <= M * (1 - z[i]) for i in Plantas for t in Tiempo), name = "R7.2")

model.addConstrs((ii[r,t+1] == ii[r,t] + quicksum((x[i,t] + h[i,t])* air[i,r] for i in Plantas) - d[r,t]*a[r] for t in range(2, 19 + 1) for r in Region), name = "R8.1")
model.addConstrs((ii[r,1] == 0 for r in Region), name = "R8.2")

model.addConstrs((ii[r,t] <= capi[r] for r in Region for t in Tiempo), name = "R9")


# #FUNCION OBJETIVO

objetivo = quicksum(l[i] * z[i] + zpl[i]*cdz[i] + (1 - zpl[i])*cfz[i] + quicksum(h[i,t] * cnt[i,t] + m[i,t] * (x[i,t] + h[i,t]) + ca[i,t] * x[i,t] + cta[i,t] * y[i,t] + ce[i,t] * (x[i,t] + h[i,t]) + cf[i,t] for t in Tiempo) for i in Plantas) + quicksum(ii[r, t] * cii[t] for t in Tiempo for r in Region)

model.setObjective(objetivo, GRB.MINIMIZE)

#OPTIMIZA
model.optimize()

solucion_optima = model.ObjVal


print('\n########################## COSTOS FINALES ##########################\n')


print(f'\nEl gasto total que se realizo durante {len(Tiempo)} años, es {round(solucion_optima, 3)} MM $US.\n')

region = {(r): ["Arica", "Tarapaca", "Antofagasta", "Atacama", "Coquimbo", "Valparaiso", "RM", "Bernardo Oh", "Maule", "Ñuble", "Bio Bio", "Araucania", "Los Rios", "Los Lagos", "Aysen", "Magallanes"][r] for r in range(1, 16)}

print('\n########################## INVERSION ##########################\n')


for i in Plantas:
    if int(z[i].x) == 1:
        print(f" La planta {i} invirtió en nueva tecnología en el periodo 1.")
print("\nEl resto de las plantas decidió no invertir en nueva tecnología.")

for t in Tiempo:
    if t != 20 and t!= 1:
        print( f'\n#################################################### AÑO {2020 + t} #################################################### \n')

    for i in Plantas:
        if int(z[i].x) == 1 and h[i,t].x > 0:
            print(f'La planta {i} produjo {round(h[i,t].x, 3)} m^3 con nueva tecnologia en el año {2020 + t}, extrayendo {round(y[i,t].x, 3)} m^3 de agua de mar.')
        elif int(z[i].x) == 0 and x[i,t].x > 0:
            print(f'La planta {i} produjo {round(x[i,t].x, 3)} m^3 con antigua tecnologia en el año {2020 + t}, extrayendo {round(y[i,t].x, 3)} m^3 de agua de mar.')
        
    for r in Region:
        if ii[r,t].x > 0:
            print(f'En la región de {region[r]} se guarda {round(ii[r,t].x, 3)} m^3 de agua desalinizada en el año {2020 + t}.')

print('\n################################ DESECHOS ################################\n')

for i in Plantas:
    if int(zpl[i].x) == 1:
        print(f'La planta {i} emitira sus desechos dentro de la zona de proteccion litoral')