Algoritmo Inicio_calificacion_final
	Escribir 'Se calcular� su calificaci�n final en la materia de algoritmos'
	Escribir 'Ingrese su calificaci�n de su primer parcial'
	Leer parcial_1
	Escribir 'Ingrese su calificaci�n de su segundo parcial'
	Leer parcial_2
	Escribir 'Ingrese su calificaci�n de su tercer parcial'
	Leer parcial_3
	Escribir 'Ingrese su calificaci�n de su examen final'
	Leer examen
	Escribir 'Ingrese su calificaci�n de su trabajo final'
	Leer trabajo
	promedio<-(parcial_1+parcial_2+parcial_3)/3
	porcentaje_promedio<-promedio*0.55
	porcentaje_examen<-examen*0.30
	porcentaje_trabajo<-trabajo*0.15
	nota<-porcentaje_examen+porcentaje_promedio+porcentaje_trabajo
	Escribir 'Su calificaci�n final es: ' nota
FinAlgoritmo
