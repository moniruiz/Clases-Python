#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, 
#separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta

productos = input("Introduce los productos de la cesta de la compra, separados por comas: ")

lista = productos.split(',')

print("Productos en tu cesta:")
for producto in lista:
    print(producto)
