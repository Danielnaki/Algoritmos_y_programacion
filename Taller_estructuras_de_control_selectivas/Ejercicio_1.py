"""
Entradas
Dinero_invertido-->float-->dinero_invertido
procentaje_banco-->float-->porcentaje_banco
Salidas
porcentaje_intereses_generados-->float-->porcentaje
ganancias-->float-->ganancias
"""
dinero_invertido=float(input("Ingrese la cantidad de dinero que invirtió "))
porcentaje_banco=float(input("Ingrese la cantidad del porcentaje aplicado por el banco "))
porcentaje_aplicado=porcentaje_banco/100
porcentaje=porcentaje_aplicado*dinero_invertido
ganancias=porcentaje+dinero_invertido
if porcentaje>=100000:
    print("Si puede reinvertir ")
else: print("No puede reinvertir ")
print("Las ganancias finales son de "+str(ganancias)+" COP")