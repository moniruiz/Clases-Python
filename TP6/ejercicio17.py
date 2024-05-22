#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
#rectángulo como el de más abajo.
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1

numero = int(input("Introduce un número entero: "))

if numero > 0:
    for i in range(1, numero +1):
        linea = []
        for j in range(2* i -1,0,-2):  #descendente
            linea.append(str(j))
        print(" ".join(linea))
else:
    print("El numero no es correcto")
