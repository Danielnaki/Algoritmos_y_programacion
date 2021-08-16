"""
Entradas
Precio_pagado-->float-->p_pa
precio_publico-->float-->p_pu
Salidas
descuento_aplicado-->float-->p_de
"""
p_pa=float(input("Precio pagado con el descuento "))
p_pu=float(input("Precio del producto en publico "))
p_de=abs(((p_pa/p_pu)*100)-100)
print("El descuento aplicado al producto es: "+str(p_de)+" %")