import math

opcion= int (input("Elige un ejercicio\n 1-Ejercicio\n 2-Ejercicio\n 3-Ejercicio\n 4-Ejercicio\n 5-Ejercicio\n 6-Ejercicio\n"))

match opcion:
    case 1:
        a=int(input("pon A\n"))
        b= int(input("pon B\n"))
        a,b=b,a   
        print("a es",a)
        print("b es",b)
    case 2:
       
        suma=0
        resta=0
        multiplicacion=0
        division=0

        a= int(input("pon A\n"))
        b= int(input("pon B\n"))
        c= int(input("pon C\n"))

        multiplicacion=a*b
        suma=a+b
        resta=a-b

        if a<=0 or b<=0:
            print("no es divisible la division",division)

        else:
            division=a/b

        print("multiplicacion",multiplicacion)
        print("suma",suma)
        print("resta",resta)
        print("division",division)

    case 3:

        a= int(input("pon A\n"))
        b= int(input("pon B\n"))

        if a==b:
            print("a es igual a b")
        else:
            if a>b:
                print("a es mayor que b")
            else:
                print("b es mayor que a")

    case 4:
        d= int(input("pon D\n"))
        e= int(input("pon E\n"))
        f= int(input("pon F\n"))

        if d>e and d>f:
            print("el numero a es el mayor")
        else:
            if e>d and e>f:
                print("el numero b es el mayor")
            else:
                print("el numero c es el mayor")    
    case 5:
        a= int(input("pon A\n"))
        b= int(input("pon B\n"))
        c= int(input("pon C\n"))
        
        if a<0:
            resultado=a*b*c

        else:
            resultado=a+b+c    

        print("el resultado es",resultado)        
    case 6:
        g= int(input("pon G\n"))

        if g<=0:
            print("error")
            
        else:
            potencia=(math.pow(g,0.5))
            raiz=math.sqrt(g)
            print(f"Del número {g} su potencia es {potencia} y su raíz {raiz}")
    case _:
        print("Elige una opcion correcta")        





