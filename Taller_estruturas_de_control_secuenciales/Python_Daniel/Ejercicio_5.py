"""
Entradas
parcial_uno-->float-->parcial_uno
parcial_dos-->float-->parcial_dos
parcial_tres-->float-->parcial_tres
examen-->float-->examen_f
trabajo-->float-->trabajo_f
Salidas
promedio-->float-->promedio_f
"""
parcial_uno=float(input("Ingrese el valor de su primer parcial "))
parcial_dos=float(input("Ingrese el valor de su segundo parcial "))
parcial_tres=float(input("Ingrese el valor de su tercer parcial "))
examen_f=float(input("Ingrese el valor de su examen final "))
trabajo_f=float(input("Ingrese el valor de su trabajo final "))
promedio_f=((parcial_uno+parcial_dos+parcial_tres)/3)*0.55+examen_f*0.3+trabajo_f*0.15
print("El promedio final del alumno es "+str(promedio_f))