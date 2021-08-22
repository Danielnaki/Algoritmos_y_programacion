"""
Entradas
Salario_vendedores-->float-->salario_vendedores
ingresos_departamento_uno-->float-->ingresos_departamento_uno
ingresos_departamento_dos-->float-->ingresos_departamento_dos
ingresos_departamento_tres-->float-->ingresos_departamento_tres
Salidas
salario_empleados_departamento_uno-->float-->salario_empleados_departamento_uno
salario_empleados_departamento_dos-->float-->salario_empleados_departamento_dos
salario_empleados_departamento_tres-->float-->salario_empleados_departamento_tres
"""
salario_vendedores=float(input("Ingrese el salario que ganan todos los empleados "))
ingresos_departamento_uno=float(input("Ingrese la cantidad de ingresos generados por el departamento uno "))
ingresos_departamento_dos=float(input("Ingrese la cantidad de ingresos generados por el departamento dos "))
ingresos_departamento_tres=float(input("Ingrese la cantidad de ingresos generados por el departamento tres "))
ingresos_totales=(ingresos_departamento_uno+ingresos_departamento_dos+ingresos_departamento_tres)*0.33
if ingresos_departamento_uno>ingresos_totales:
    salario_empleados_departamento_uno=salario_vendedores+(salario_vendedores*0.2)
else: salario_empleados_departamento_uno=salario_vendedores
if ingresos_departamento_dos>ingresos_totales:
    salario_empleados_departamento_dos=salario_vendedores+(salario_vendedores*0.2)
else: salario_empleados_departamento_dos=salario_vendedores
if ingresos_departamento_tres>ingresos_totales:
    salario_empleados_departamento_tres=salario_vendedores+(salario_vendedores*0.2)
else: salario_empleados_departamento_tres=salario_vendedores
print("el salario de los empleados del departamento uno es: "+str(salario_empleados_departamento_uno)+" COP")
print("el salario de los empleados del departamento dos es: "+str(salario_empleados_departamento_dos)+" COP")
print("el salario de los empleados del departamento tres es: "+str(salario_empleados_departamento_tres)+" COP")