Algoritmo Inicio_minutos_horas
	Escribir 'Escribe los minutos que se convertirán a horas'
	Escribir 'Ingresa el total de minutos'
	leer minutos
	horas<-minutos/60
	minutos_restantes<-minutos MOD 60
	Escribir 'El total es: ' trunc(horas) ' horas y ' minutos_restantes ' minutos'
FinAlgoritmo
