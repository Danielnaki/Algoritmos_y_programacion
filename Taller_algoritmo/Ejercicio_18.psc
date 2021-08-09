Algoritmo Inicio_iniciales_nombre
	Escribir 'Ingrese su primer nombre'
	Leer p_nombre
	Escribir 'Ingrese su segundo nombre'
	Leer s_nombre
	Escribir 'Ingrese su primer apellido'
	Leer p_apellido
	Escribir 'Ingrese su segundo apellido'
	Leer s_apellido
	pi_nombre<-Subcadena(p_nombre,0,0)
	si_nombre<-Subcadena(s_nombre,0,0)
	pi_apellido<-Subcadena(p_apellido,0,0)
	si_apellido<-Subcadena(s_apellido,0,0)
	Escribir 'Las iniciales de su nombre son: ' Mayusculas(pi_nombre) Mayusculas(si_nombre) Mayusculas(pi_apellido) Mayusculas(si_apellido)
FinAlgoritmo
