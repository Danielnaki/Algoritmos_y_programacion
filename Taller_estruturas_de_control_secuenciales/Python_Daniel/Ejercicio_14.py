"""
Entradas
lectura_anterior-->float-->l_an
lectura_actual-->float-->l_ac
costo_kilovatio-->float-->c_k
Salidas
total_pagar-->floa-->t_p
"""
l_an=float(input("Ingrese la lectura anterior del recibo de la luz "))
l_ac=float(input("Ingrese la lectura actual del recibo de la luz "))
c_k=float(input("Ingrese el valor por kilovatio "))
t_p=(l_an*c_k)+(l_ac*c_k)
print("El total a pagar es: "+str(t_p))