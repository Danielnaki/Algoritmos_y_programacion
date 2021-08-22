"""
Entradas
Sueldo_trabajador-->float-->sueldo_trabajador
Salidas
sueldo_neto-->float-->sueldo_neto
"""
sueldo_trabajador=float(input("Ingrese el sueldo del trabajador "))
if sueldo_trabajador<900000:
    sueldo_neto=(sueldo_trabajador*0.15)+sueldo_trabajador
else: sueldo_neto=(sueldo_trabajador*0.12)+sueldo_trabajador
print("El nuevo sueldo del trabajador es: "+str(sueldo_neto)+" COP")