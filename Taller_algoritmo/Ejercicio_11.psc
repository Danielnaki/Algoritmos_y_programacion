Algoritmo Inicio_calificacion_final
	Escribir 'Se calculará su calificación final en la materia de algoritmos'
	Escribir 'Ingrese su calificación de su primer parcial'
	Leer parcial_1
	Escribir 'Ingrese su calificación de su segundo parcial'
	Leer parcial_2
	Escribir 'Ingrese su calificación de su tercer parcial'
	Leer parcial_3
	Escribir 'Ingrese su calificación de su examen final'
	Leer examen
	Escribir 'Ingrese su calificación de su trabajo final'
	Leer trabajo
	promedio<-(parcial_1+parcial_2+parcial_3)/3
	porcentaje_promedio<-promedio*0.55
	porcentaje_examen<-examen*0.30
	porcentaje_trabajo<-trabajo*0.15
	nota<-porcentaje_examen+porcentaje_promedio+porcentaje_trabajo
	Escribir 'Su calificación final es: ' nota
FinAlgoritmo
