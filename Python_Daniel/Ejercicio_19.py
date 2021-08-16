"""
Entradas
cantidad_producto-->int-->c_p
Precio_por_docena-->float-->precio_d
ganancias-->float-->g
Salidas
porcentaje_ganancias-->float-->p_g
"""
c_p=int(input("Ingrese la cantidad de productos comprados "))
precio_d=float(input("Cúal es el precio por docena de los productos "))
g=float(input("Cúales fueron las ganancias producidas por los productos "))
gastos=c_p*(precio_d/12)
p_g=((g-gastos)/gastos)*100
print("El Porcentaje de ganancias es del "+str(p_g)+" %")