"""
Entradas
capital_prestado-->float-->c_p
tiempo_interes-->int-->t_i
interes-->float-->i
Salidas
porcentaje_anual-->float-->p_a
"""
c_p=float(input("Cúal es la cantidad del prestamo realizado "))
t_i=int(input("A cúantos años de interes se realizó el prestamo "))
i=float(input("Cúal es la cantidad total del capital pagado "))
p_a=(i*100)/(t_i*c_p)
print("El procentaje de interes anual es de: "+str(p_a)+" %")