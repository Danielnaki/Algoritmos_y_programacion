Algoritmo Ejercicio_11
	Escribir "Ingrese el nombre del trabajador "
	leer n_trabajador
	Escribir "Ingrese el sueldo base del trabajador "
	leer sueldo_b
	Escribir "Ingrese el valor por hora normal "
	leer p_horas_n
	Escribir "Ingrese la cantidad de horas normales trabajadas "
	leer horas_n
	Escribir "Ingrese la cantidad de horas extras trabajadas "
	leer horas_e
	Escribir "Ingrese la cantidad de actualizaciones academicas hechas por el trabajador "
	leer n_update_a
	Escribir "Ingrese la cantidad de hijos del trabajador "
	leer n_hijos
	horas_extras=(p_horas_n*0.25)*horas_e
	horas_trabajadas=horas_n*p_horas_n
	asignacion=(250000*n_update_a)+(173000*n_hijos)+180000
	deduccion=((sueldo_b*0.05)+(sueldo_b*0.02)+(sueldo_b*0.07))
	sueldo_n=sueldo_b+asignacion+horas_extras+horas_trabajadas-deduccion
	escribir "Las asignaciones del trabajador son: " asignacion 
	escribir "Las deducciones del trabajador son: " deduccion
	escribir "El sueldo neto del trabajador " n_trabajador " en el mes de diciembre es: " sueldo_n
FinAlgoritmo