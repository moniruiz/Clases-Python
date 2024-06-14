#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número 
#primo o no

numero = int(input("Ingrese un numero entero: "))
c = 0

for i in range (1, numero+1):
    if numero%i == 0:
        c= c+1

if c>2:
    print("No es primo")
else:
    print("Es primo ")