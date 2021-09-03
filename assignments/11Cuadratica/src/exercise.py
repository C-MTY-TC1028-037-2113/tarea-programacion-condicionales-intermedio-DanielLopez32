def main():
    # Escribe tu código abajo de esta línea
    a=int(input("Da el valor de a: "))
    b=int(input("Da el valor de b: "))
    c=int(input("Da el valor de c: "))
    if (a==0) and (b==0):
        print("No tiene solucion")
    elif (a==0):
        raiz=-c/b
        print(raiz)
    else:
        discrim=b**2-4*a*c
        if (discrim)>0:
            x1=(-b+((discrim)**0.5))/(2*a)
            x2=(-b-((discrim)**0.5))/(2*a)
            print(x1)
            print(x2)
        elif (discrim < 0):
            print("Raices complejas")
        else:
            x=-b/(2*a)
            print(x)

if __name__ == '__main__':
    main()
