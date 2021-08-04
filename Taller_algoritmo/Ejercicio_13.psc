Algoritmo Inicio_distancia_numeros
	Escribir 'Este algoritmo hallará la distancia de dos pares de números'
	Escribir 'Ingresar el primer número de la primera pareja de numeros'
	Leer numero_1_1
	Escribir 'Ingresar el segundo número de la primera pareja de numeros'
	Leer numero_2_1
	Escribir 'Ingresar el primer número de la segunda pareja de numeros'
	Leer numero_1_2
	Escribir 'Ingresar el segundo número de la segunda pareja de numeros'
	Leer numero_2_2
	distancia<-raiz((numero_2_1-numero_1_1)^2+(numero_1_2-numero_2_2)^2)
	Escribir 'La distancia de los dos números es: ' distancia
FinAlgoritmo
