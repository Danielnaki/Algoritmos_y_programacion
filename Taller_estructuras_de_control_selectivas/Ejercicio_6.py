"""
Entradas
dato_a-->int-->A
dato_b-->int-->B
dato_c-->int-->C
dato_d-->int-->D
Salidas
numero_N-->int-->N
"""
A=int(input("Ingrese el valor del dato A "))
B=int(input("Ingrese el valor del dato B "))
C=int(input("Ingrese el valor del dato C "))
D=int(input("Ingrese el valor del dato D "))
N=int(str(A)+str(B)+str(C)+str(D))
if C>5 and B<9:
    N=(str(A)+str(B+1)+str(C*0)+str(D*0))
    print(N)
elif C>5 and B>=9:
    N=str(A+1)+str(B*0)+str(C*0)+str(D*0)
    print(N)
elif C<5 and B==9:
    N=str(A)+str(B)+str(C*0)+str(D*0)
    print(N)
elif C<5 and B<9:
    N=(str(A)+str(B)+str(C*0)+str(D*0))
    print(N)
elif D>0:
    N=(str(A)+str(B)+str(C)+str(D*0))
    print(N)
else: print(N)