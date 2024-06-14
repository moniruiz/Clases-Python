#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

palabra = input("Introduce una palabra para verificar si es palindromo: ")

if palabra.strip() == palabra[::-1]:
    print(f"la palabra {palabra} es palindromo")
else:
    print("No es palindromo")