"""
Entradas
nombre_trabajador-->str-->n_trabajador
Sueldo_base-->float-->sueldo_b
precio_hora_normal-->float-->p_hora_n
horas_normales_trabajo-->int-->horas_n
horas_extra_trabajo-->int-->horas_e
número_actualización_academica-->int-->n_update_a
número_hijos-->int-->n_hijos
Salidas
asignaciones-->float-->asignacion
deducciones-->float-->deducccion
sueldo_neto-->float-->sueldo_n
"""
n_trabajador=str(input("Ingrese el nombre del trabajador "))
sueldo_b=float(input("Ingrese el sueldo base del trabajador "))
p_horas_n=float(input("Ingrese el valor por hora normal "))
horas_n=int(input("Ingrese la cantidad de horas normales trabajadas "))
horas_e=int(input("Ingrese la cantidad de horas extras trabajadas "))
n_update_a=int(input("Ingrese la cantidad de actualizaciones academicas hechas por el trabajador "))
n_hijos=int(input("Ingrese la cantidad de hijos del trabajador "))
horas_extras=(p_horas_n*0.25)*horas_e
horas_trabajadas=horas_n*p_horas_n
asignacion=(250000*n_update_a)+(173000*n_hijos)+180000
deduccion=((sueldo_b*0.05)+(sueldo_b*0.02)+(sueldo_b*0.07))
sueldo_n=sueldo_b+asignacion+horas_extras+horas_trabajadas-deduccion
print("Las asignaciones del trabajador son: "+str(asignacion))
print("Las deducciones del trabajador son: "+str(deduccion))
print("El sueldo neto del trabajador "+str(n_trabajador)+" en el mes de diciembre es: "+str(sueldo_n))