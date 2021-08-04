Algoritmo Inicio_sueldo_comicion
	Escribir 'Se calculará su sueldo mensual más las comiciones por venta'
	Escribir 'Ingrese el valor de su sueldo base'
	leer sueldo
	Escribir 'Ingrese el número de ventas realizadas'
	leer ventas
	comicion<-sueldo*0.1
	g_comicion<-comicion*ventas
	sueldo_total<-sueldo+g_comicion
	Escribir 'El valor de las comiciones es: ' g_comicion
	Escribir 'Su sueldo en el mes es: ' sueldo_total
FinAlgoritmo
