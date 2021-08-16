Algoritmo Ejercicio_12
	Escribir "Ingrese la nota del examen de matematicas "
	leer e_mate
	Escribir "Ingrese la nota de la primera tarea de matematicas "
	leer t_mate_uno
	Escribir "Ingrese la nota de la segunda tarea de matematicas "
	leer t_mate_dos
	Escribir "Ingrese la nota de la tercera tarea de matematicas "
	leer t_mate_tres
	Escribir "Ingrese la nota del examen de quimica "
	leer e_quim
	Escribir "Ingrese la nota de la primera tarea de quimica "
	leer t_quim_uno
	Escribir "Ingrese la nota de la segunda tarea de quimica "
	leer t_quim_dos
	Escribir "Ingrese la nota del examen de fisica "
	leer e_fis
	Escribir "Ingrese la nota de la primera tarea de fisica "
	leer t_fis_uno
	escribir "Ingrese la nota de la segunda tarea de fisica "
	leer t_fis_dos
	Escribir "Ingrese la nota de la tercera tarea de fisica "
	leer t_fis_tres
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
escribir "El promedio de Matematicas es: " prom_mate
escribir "El promedio de Quimica es: " prom_quim
escribir "El promedio de Fisica es: " prom_fis
escribir "El promedio general de las materias es: " prom_gen
FinAlgoritmo