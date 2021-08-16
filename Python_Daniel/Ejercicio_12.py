"""
Entradas
Examen_matematicas-->float-->e_mate
tarea_uno_matematicas-->float-->t_mate_uno
tarea_dos_matematicas-->float-->t_mate_dos
tarea_tres_matematicas-->float-->t_mate_tres
Examen_quimica-->float-->e_quim
tarea_uno_quimica-->float-->t_quim_uno
tarea_dos_quimica-->float-->t_quim_dos
Examen_fisica-->float-->e_fis
tarea_uno_fisica-->float-->t_fis_uno
tarea_dos_fisica-->float-->t_fis_dos
tarea_tres_fisica-->float-->t_fis_tres
Salidas
promedio_general-->float-->prom_gen
promedio_matematicas-->float-->prom_mate
promedio_quimica-->float-->prom_quim
promedio_fisica-->float-->prom_fis
"""
e_mate=float(input("Ingrese la nota del examen de matematicas "))
t_mate_uno=float(input("Ingrese la nota de la primera tarea de matematicas "))
t_mate_dos=float(input("Ingrese la nota de la segunda tarea de matematicas "))
t_mate_tres=float(input("Ingrese la nota de la tercera tarea de matematicas "))
e_quim=float(input("Ingrese la nota del examen de quimica "))
t_quim_uno=float(input("Ingrese la nota de la primera tarea de quimica "))
t_quim_dos=float(input("Ingrese la nota de la segunda tarea de quimica "))
e_fis=float(input("Ingrese la nota del examen de fisica "))
t_fis_uno=float(input("Ingrese la nota de la primera tarea de fisica "))
t_fis_dos=float(input("Ingrese la nota de la segunda tarea de fisica "))
t_fis_tres=float(input("Ingrese la nota de la tercera tarea de fisica "))
E_mate=e_mate*0.9
p_mate=((t_mate_uno+t_mate_dos+t_mate_tres)/3)*0.1
prom_mate=E_mate+p_mate
E_quim=e_quim*0.85
p_quim=((t_quim_uno+t_quim_dos)/2)*0.15
prom_quim=E_quim+p_quim
E_fis=e_fis*0.8
p_fis=((t_fis_uno+t_fis_dos+t_fis_tres)/3)*0.2
prom_fis=E_fis+p_fis
prom_gen=(prom_mate+prom_fis+prom_quim)/3
print("El promedio de Matematicas es: "+str(prom_mate))
print("El promedio de Quimica es: "+str(prom_quim))
print("El promedio de Fisica es: "+str(prom_fis))
print("El promedio general de las materias es: "+str(prom_gen))