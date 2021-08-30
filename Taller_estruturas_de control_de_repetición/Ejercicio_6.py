division=input("Ingrese los numeros a ser divididos separados por (/) ").split("/")
dividendo, divisor=division
dividendo=int(dividendo)
divisor=int(divisor)
cociente=1
cociente_cero=0
residuo=dividendo%divisor
print(dividendo)
while (dividendo>divisor):
    if dividendo>0 and residuo==0:
        dividendo=dividendo-divisor
        cociente=cociente+1
        print(dividendo)
    elif dividendo>0 and residuo>0:
        dividendo=dividendo-divisor
        cociente_cero=cociente_cero+1
        print(dividendo)
    elif dividendo==0:
        break
print(residuo)
if dividendo>0 and residuo==0:
    print("El cociente de la division es: "+str(cociente))
    print("El residuo de la division es: "+str(residuo))
else:
    print("El cociente de la division es: "+str(cociente_cero))
    print("El residuo de la division es: "+str(residuo))