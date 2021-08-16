"""
Entradas
Billetes_50000-->int-->N1
Billetes_20000-->int-->N2
Billetes_10000-->int-->N3
Billetes_5000-->int-->N4
Billetes_2000-->int-->N5
Billetes_1000-->int-->N6
Billetes_500-->int-->N7
Billetes_100-->int-->N8
Salidas
Cantidad_dinero-->float-->c_d
"""
N1=int(input("Ingrese la cantidad de billetes de 50000 "))
N2=int(input("Ingrese la cantidad de billetes de 20000 "))
N3=int(input("Ingrese la cantidad de billetes de 10000 "))
N4=int(input("Ingrese la cantidad de billetes de 5000 "))
N5=int(input("Ingrese la cantidad de billetes de 2000 "))
N6=int(input("Ingrese la cantidad de billetes de 1000 "))
N7=int(input("Ingrese la cantidad de billetes de 500 "))
N8=int(input("Ingrese la cantidad de billetes de 100 "))
c_d=(N1*50000)+(N2*20000)+(N3*10000)+(N4*5000)+(N5*2000)+(N6*1000)+(N7*500)+(N8*100)
print("El banco cuenta con la siguente cantidad de dinero: "+str(c_d))