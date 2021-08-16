"""
Entradas
metros-->float-->m
Salidas
pies-->float-->pies
pulgadas-->float-->pulgada
"""
m=float(input("Ingrese la cantidad de metros a convertir "))
pulgada=float(m*39.37)
pies=float(pulgada/12)
print("Ese dato equivale a "+str(pulgada)+" Pulgadas")
print("Ese dato equivale a "+"{:.4f}".format(pies)+" Pies")