"""
Entradas
lado_a-->float-->a
lado_b-->float-->b
lado_b-->float-->c
Salidas
area-->float-->area
"""
a=float(input("Ingrese la longitud del lado A del triangulo "))
b=float(input("Ingrese la longitud del lado B del triangulo "))
c=float(input("Ingrese la longitud del lado c del triangulo "))
s=float((a+b+c)/2)
area=float((s*(s-a)*(s-b)*(s-c))**0.5)
print("El area del triangulo es: "+str(area))