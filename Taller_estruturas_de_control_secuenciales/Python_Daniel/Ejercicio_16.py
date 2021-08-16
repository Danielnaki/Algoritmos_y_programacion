"""
Entradas
litros-->float-->l
Salidas
litros_comprados-->float-->l_c
Nota:
    1 Galon= 3.785 Litro
    1 litro = 50000 COP
"""
l=float(input("Ingrese la cantidad de litros comprados "))
l_c=(l/3.785)*(3.785*50000)
print("El total a pagar es: "+str(l_c)+" COP")
