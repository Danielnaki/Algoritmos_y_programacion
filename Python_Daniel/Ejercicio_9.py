"""
Entradas
sueldo_base-->float-->sueldo_b
horas_trabajadas-->int-->horas_t
precio_hora-->float-->p_hora
Salida
Sueldo_neto-->float-->sueldo_n
"""
sueldo_b=float(input("Ingrese su sueldo base "))
horas_t=int(input("Ingrese la cantidad de horas trabajadas "))
p_hora=float(input("Ingrese el precio de cada hora "))
d_sueldo_b=sueldo_b-(sueldo_b*0.2)
sueldo_n=(horas_t*p_hora)+d_sueldo_b
print("El sueldo neto del trabajador es: "+str(sueldo_n))