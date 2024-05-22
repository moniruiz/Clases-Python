cantidad = int(input("ingrese la cantidad a invertir"))
interes = int(input("ingrese el interes"))
anios= int(input("ingrese la cantidad de años a invertir"))

cantidadCobrar = (cantidad * interes)/100
total= cantidadCobrar * anios

print(total)