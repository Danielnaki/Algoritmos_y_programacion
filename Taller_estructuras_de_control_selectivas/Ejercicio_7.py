"""
Entradas
Kilometros-->int-->kilometro
Salidas
pagos_clientes-->float-->pagos_clientes
"""
kilometros=int(input("Ingrese la cantidad de Kilometros "))
if kilometros<=300:
    pagos_clientes=50000
    print("Al cliente le corresponde pagar "+str(pagos_clientes)+" COP")
elif kilometros>300 and kilometros<1000:
    pagos_clientes=70000+((kilometros-300)*30000)
    print("Al cliente le corresponde pagar "+str(pagos_clientes)+" COP")
elif kilometros>1000:
    pagos_clientes=150000+((kilometros-1000)*9000)
    print("Al cliente le corresponde pagar "+str(pagos_clientes)+" COP")