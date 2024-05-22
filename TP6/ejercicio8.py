#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere 
#calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe 
#preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 
#años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500.00 y si es mayor de 18 años, $ 
#1000.00

edad = int(input("Ingrese la edad del cliente: "))

if edad < 4:
    precio = 0 
elif edad <= 18:
    precio = 500.00 
else:
    precio = 1000.00 

if precio == 0:
    print("El cliente puede entrar gratis.")
else:
    print(f"El precio de la entrada es: ${precio:.2f}")
