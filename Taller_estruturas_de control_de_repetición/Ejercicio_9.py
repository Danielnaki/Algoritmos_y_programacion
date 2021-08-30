tipo=0
alcohol=0
gasolina=0
diesel=0
while True:
    tipo=int(input(""))
    if tipo==1:
        alcohol=alcohol+1
    elif tipo==2:
        gasolina=gasolina+1
    elif tipo==3:
        diesel=diesel+1
    elif tipo==4:
        break
print("MUITO OBRIGADO")
print("Alcool: "+str(alcohol))
print("Gasolina: "+str(gasolina))
print("Diesel: "+str(diesel))