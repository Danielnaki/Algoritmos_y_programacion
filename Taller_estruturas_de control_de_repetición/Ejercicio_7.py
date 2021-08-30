while True:
    Valores=input().split(" ")
    X, M=Valores
    X=int(X)
    M=int(M)
    if (0<X<=3 and 10<=M<=2**32-1):
        Exp=M*X
        print(Exp)
    elif X==0 and M==0:
        break