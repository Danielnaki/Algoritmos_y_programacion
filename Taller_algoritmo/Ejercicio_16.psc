Algoritmo Inicio_invertir_dos_numero
	Escribir 'Escribe el primer n�mero de dos cifras para ser invertido'
	Leer numero_1
	Escribir 'Escribe el segundo n�mero de dos cifras para ser invertido'
	Leer numero_2
	primer_numero<-Subcadena(numero_1,0,0)
	ultimo_numero<-Subcadena(numero_1,1,1)
	primer_numero_2<-Subcadena(numero_2,0,0)
	ultimo_numero_2<-Subcadena(numero_2,1,1)
	Escribir 'El primer n�mero invertido es: ' ultimo_numero primer_numero
	Escribir 'El segundo n�mero invertido es: ' ultimo_numero_2 primer_numero_2
	Escribir 'Los dos n�meros juntos son: ' numero_1 numero_2
	Escribir 'Los dos n�meros invertidos juntos son: ' ultimo_numero_2 primer_numero_2 ultimo_numero primer_numero
FinAlgoritmo
