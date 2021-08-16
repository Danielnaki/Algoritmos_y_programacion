"""
Entradas
Numero_hombres-->int-->n_hombres
Numero_mujeres-->int-->n_mujeres
Salidas
porcentaje_hombres-->float-->p_hombres
porcentaje_mujeres-->float-->p_mujeres
"""
n_hombres=int(input("Ingrese el número de hombres "))
n_mujeres=int(input("Ingrese el número de mujeres "))
total=int(n_hombres+n_mujeres)
p_h=float(n_hombres/total)
p_m=float(n_mujeres/total)
p_hombres=float(p_h*100)
p_mujeres=float(p_m*100)
print("El porcentaje de los hombres es: "+str(p_hombres)+" %")
print("El porcentaje de las mujeres es: "+str(p_mujeres)+" %")