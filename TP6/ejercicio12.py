#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos 
#los números impares desde 1 hasta ese número separados por comas.

numero = int(input("Ingrese un numero: "))

if numero > 0:
        impares =[]
        for i in range(1, numero+1):
                if  i %2 !=0 :
                        impares.append(str(i))
        
        resultado = ",".join(impares)
        print(resultado)
else:
        print("El numero ingresado no es correcto")