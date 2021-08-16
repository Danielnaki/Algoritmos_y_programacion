"""
Entradas
valor-->float-->valor
Salidas
Descuento-->float-->descuento
"""
print("Se realizará un descuento del 15%")
valor=float(input("Ingrese el valor del producto "))
descuento=valor-valor*0.15
print("El total a pagar por el producto es: "+str(descuento))