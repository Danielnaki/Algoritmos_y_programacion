"""
Entradas
Sueldo-->float-->sueldo
ventas-->int-->ventas
Salidas
ganancias-->float-->g_comicion
Sueldo+Comiciones-->float-->sueldo_f
"""
sueldo=float(input("Ingrese su sueldo "))
ventas=int(input("Ingrese el numero de ventas realizadas "))
g_comicion=ventas+(sueldo*0.1)
sueldo_f=sueldo+g_comicion
print("Las ganancias por ventas son: "+str(g_comicion))
print("Su sueldo final es: "+str(sueldo_f))