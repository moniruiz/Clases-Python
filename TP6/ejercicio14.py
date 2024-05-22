#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número 
#de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

cantidad = int(input("ingrese la cantidad a invertir"))
interes = int(input("ingrese el interes"))
anios= int(input("ingrese la cantidad de años a invertir"))

cantidad_cobrar = (cantidad * interes)/100
total= cantidad_cobrar * anios

print(total)