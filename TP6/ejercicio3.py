#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el 
#divisor es cero el programa debe mostrar un error.

num1 = float(input("Introduce un numero: "))
num2 = float(input("Introduce el numero por el que se va a dividir: "))

if num2 == 0:
    print("No se puede dividir por 0")
else:
    resultado = num1 / num2
    print("El resultado de la división es:", resultado)
