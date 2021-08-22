"""
Entradas
total_del_monto_comprado-->float-->total_comprado
Salidas
cantidad_invertida_empresa-->float-->total_empresa
cantidad_pagar_credito-->float-->total_credito
cantidad_pagar_intereses-->float-->total_intereses
cantidad_prestada_banco-->float-->total_banco
"""
total_comprado=float(input("Ingrese la cantidad de dinero a pagar por las piezas compradas "))
if total_comprado>5000000:
    total_empresa=total_comprado*0.55
    total_banco=total_comprado*0.3
    fabricante=total_comprado*0.15
    total_intereses=fabricante*0.2
    print("La cantidad invertida de los fondos de la empresa es: "+str(total_empresa)+" COP")
    print("La cantidad prestada por el banco es: "+str(total_banco)+" COP")
    print("La cantidad a pagar por credito del fabricante es: "+str(fabricante)+" COP")
    print("La cantidad total por pagar al fabricante por intereses del 20 % es: "+str(total_intereses)+" COP")
elif total_comprado<=5000000:
    total_empresa=total_comprado*0.7
    fabricante=total_comprado*0.3
    total_intereses=fabricante*0.2
    print("La cantidad invertida de los fondos de la empresa es: "+str(total_empresa)+" COP")
    print("La cantidad a pagar por credito del fabricante es: "+str(fabricante)+" COP")
    print("La cantidad total por pagar al fabricante por intereses del 20 % es: "+str(total_intereses)+" COP")