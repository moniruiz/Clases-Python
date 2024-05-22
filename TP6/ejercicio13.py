#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la 
#cuenta atrás desde ese número hasta cero separados por comas.

numero = int(input("Ingrese un numero enter positivo: "))

if numero > 0:
    cuenta= []
    for i in range(numero, -1 ,-1):
        cuenta.append(str(i))

    resultado = ",".join(cuenta)
    print(resultado)
else:
    print("El numero ingresado no es correcto")