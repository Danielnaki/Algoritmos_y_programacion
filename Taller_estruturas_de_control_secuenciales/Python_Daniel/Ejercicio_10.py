"""
Entradas
chelines_austriacos-->float-->c_a
dracmas_griegos-->float-->d_g
pesetas-->float-->p
Salidas
pesetas-->float-->p_s
francos_franceses-->float-->f_f
dolares-->float-->USD
liras_italianas-->float-->l_i
"""
"""
100 chelines austríacos = 956.871 pesetas
1 dólar EEUU = 122.499 pesetas
100 dracmas griegos = 88.607 pesetas
100 francos belgas = 323.728 pesetas
1 franco francés = 20.110 pesetas
1 libra esterlina = 178.938 pesetas
100 liras italianas = 9.289 pesetas
"""
c_a=float(input("Ingrese la cantidad de Chelines Austriacos que serán convertidos a Pesetas "))
d_g=float(input("Ingrese la cantidad de Dracmas Griegos que serán convertidos a Francos Franceses "))
p=float(input("Ingrese la cantidad de Pesetas que serán covertidas a Dólares y Liras Italianas "))
p_s=c_a*(956.871/100)
f_f=(d_g*(88.607/100))/20.110
USD=p/122.499
l_i=p/(9.289/100)
print("El equivalente de los Chelines Austriacos es: "+str(p_s)+" Pesetas")
print("El equivalente de los Dracmas Griegos es: "+str(f_f)+" Francos Franceses")
print("El equivalente de las Pesetas es: "+str(USD)+" Dolares y "+str(l_i)+" Liras Italianas")