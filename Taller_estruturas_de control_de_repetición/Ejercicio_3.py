contador=97
suma=0
while(contador<1003):
    if(contador%2==0):
        suma=suma+contador
        contador=contador+2
        print(contador)
    else:
        contador=contador+1
print(suma)