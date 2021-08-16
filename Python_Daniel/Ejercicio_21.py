"""
Entradas
valor_contado-->float-->v_c
cantidad_cuotas-->int-->c_c
Salidas
porcentaje_cobro_cuotas-->float-->p_c_c
"""
v_c=float(input("Ingrese el valor del producto para pago de contado "))
c_c=int(input("Ingrese la cantidad de cuotas "))
v_cuota=(v_c/c_c)
c_c_c=c_c
if c_c>=12:
    p_c_c=v_cuota*0.1
    print("El porcentaje que se cobra por cada cuota es: 10 % y coresponde a "+str(p_c_c)+" COP por Cuota")
else:
    p_c_c=v_cuota*0.05
    print("El porcentaje que se cobra por cada cuota es: 5 % y coresponde a "+str(p_c_c)+" COP por Cuota")