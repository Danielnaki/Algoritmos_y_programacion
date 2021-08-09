Algoritmo Inicio_distancia_vehiculos
	Escribir 'Ingrese la velocidad (Km/h) del primer vehiculo (velocidad más baja a la del segundo vehiculo)'
	Leer velocidad_vehiculo_1
	Escribir 'Ingrese la velocidad (Km/h) del segundo vehiculo (velocidad más alta a la del primer vehiculo)'
	Leer velocidad_vehiculo_2
	Escribir 'Ingrese la distancia (Km) entre los dos vehiculos'
	Leer distancia_vehiculos
	//v=d/t
	//t=d/v
	//d_v_1=d*v_v_1/(v_V_2-v_v_1)
	//t=d_v_1/v_v_1
	distancia_vehiculo_1<-(distancia_vehiculos*velocidad_vehiculo_1)/(velocidad_vehiculo_2-velocidad_vehiculo_1)
	tiempo_vehiculo_1<-distancia_vehiculo_1/velocidad_vehiculo_1
	alcanzar_vehiculo_1<-tiempo_vehiculo_1
	minutos<-alcanzar_vehiculo_1*60
	Escribir 'El primer vehiculo es alcanzado por el segunodo vehiculo en: ' minutos ' minutos'
FinAlgoritmo
