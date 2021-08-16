Algoritmo Ejercicio_21
//Entradas
//valor_contado-->float-->v_c
//cantidad_cuotas-->int-->c_c
//Salidas
//porcentaje_cobro_cuotas-->float-->p_c_c
escribir "Ingrese el valor del producto para pago de contado "
Leer v_c
escribir "Ingrese la cantidad de cuotas "
leer c_c
v_cuota=(v_c/c_c)
c_c_c=c_c
si c_c >= 12
    p_c_c=v_cuota*0.1
	escribir "El porcentaje que se cobra por cada cuota es: 10 % y coresponde a " p_c_c " COP por Cuota"
SiNo
    p_c_c=v_cuota*0.05
    escribir "El porcentaje que se cobra por cada cuota es: 5 % y coresponde a " p_c_c " COP por Cuota"
FinAlgoritmo
