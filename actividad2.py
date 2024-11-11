import math

print("Introduce la opcion que quieras")
print("""1. Escriure un programa que permet llegir l’edat i el pes d’una
persona i després la doni per pantalla.

2. Escriure un programa que calculi l’àrea d’un triangle rebent com a
entrada la base i l’altura, i després la doni per pantalla.

3. Escriure un programa que donats dos valors d’entrada ens doni la
divisió del major i el menor.

4. Escriure un programa que llegeix l’entrada de tres nombres i que
ens doni el major d’ells.

5. Escriure un programa que llegeix dos nombres que són una data
(dia, mes). Comprovar que la data sigui vàlida i que el mes sigui
vàlid i ens avisi que la data és correcte o incorrecte.\n""")

opcion = int(input("Introduce la opcion que quieras\n"))

match opcion:

    case 1:
        print("Has elegido la opcion 1")
        edat=int(input("Introduce el edad:"))
        peso=int(input("Introduce el peso:"))

        print("La edad que has introducido es",edat)
        print("El peso que has introducido es",peso)

    case 2:
        print("Has elegido la opcion 2")
        base=int(input("Introduce la base del triangulo:"))
        altura=int(input("Introduce la altura del triangulo:"))
        resultado=0
        resultado=base*altura

        print("El resultado del area del triangulo es:",resultado)
    case 3:
        print("Has elegido la opcion 3")
        numero1 = int(input("Introduce el numero 1:"))
        numero2 = int(input("Introduce el numero 2:"))

        if(numero1 !=0 and numero2 !=0):
            if(numero1>numero2):
                print("El resultado es:"+str(numero1/numero2))
            if(numero1<numero2):
                print("El resultado es:"+str(numero2/numero1))    
        else:
            print("Inroduce un numero mayor a 0")

    case 4:
        print("Has elegido la opcion 4")

        numeros = [0, 0, 0]
        max = 0

        numero1 = int(input("Introduce el numero 1:"))
        numero2 = int(input("Introduce el numero 2:"))
        numero3 = int(input("Introduce el numero 3:"))

        numeros[0] = numero1
        numeros[1] = numero2
        numeros[2] = numero3

        for i in range(len(numeros)):
            if (numeros[i] > max):
                max = numeros[i]

        print("El numero mas grande es "+str(max))

    case 5:
        print("Has elegido la opcion 5")
        dia = int(input("Dime un número de día: "))
        mes = int(input("Dime un mes del año: "))

        dia_Meses = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if mes < 1 or mes > 12:
            print("Introduce un mes correcto")

        elif dia < 1 or dia > dia_Meses[mes - 1]:
            print("Elige un día correcto")
        else:
            print("Fecha correcta:", dia, "/", mes)
