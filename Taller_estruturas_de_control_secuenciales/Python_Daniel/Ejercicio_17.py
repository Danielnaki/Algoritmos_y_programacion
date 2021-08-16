"""
Entradas
monto_presupuestal-->float-->m_p
Salidas
correspondiente_ginecologia-->float-->c_g
correspondiente_traumatologia-->float-->c_t
correspondiente_pediatria-->float-->c_p
"""
m_p=float(input("Presupuesto anual al Hospital rural "))
c_g=m_p*0.40
c_t=m_p*0.30
c_p=m_p*0.30
print("El presupuesto correspondiente para ginecología es: "+str(c_g))
print("El presupuesto correspondiente para traumatología es: "+str(c_t))
print("El presupuesto correspondiente para pediatría es: "+str(c_p))