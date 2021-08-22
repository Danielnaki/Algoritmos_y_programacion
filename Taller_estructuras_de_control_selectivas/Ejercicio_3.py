"""
Entradas
Dato_A-->int-->dato_a
Dato_B-->int-->dato_b
Dato_C-->int-->dato_c
Dato_D-->int-->dato_d
Salidas
Resultado_primera_expresión-->int-->r_primera_e
Resultado_segunda_expresión-->float-->r_segunda_e
"""
dato_a=int(input("Ingrese el dato A "))
dato_b=int(input("Ingrese el dato B "))
dato_c=int(input("Ingrese el dato C "))
dato_d=int(input("Ingrese el dato D "))
if dato_d==0:
    r_primera_e=(dato_a-dato_c)**2
    print("El resultado de la primera expresión es: "+str(r_primera_e))
elif dato_d>0:
    r_segunda_e=float(((dato_a-dato_b)**3)/dato_d)
    print("El resultado de la segunda expresión es: "+str(r_segunda_e))
else: print("No se puede resolver según la descripcion del problema")