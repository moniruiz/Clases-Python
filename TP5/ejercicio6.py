#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y 
#después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

# Solicita al usuario que introduzca una frase
frase = input("Por favor, introduce una frase: ")

# Solicita al usuario que introduzca una vocal
vocal = input("Introduce una vocal: ")

# Verifica si la entrada es realmente una vocal y tiene longitud de un carácter
if vocal.lower() in "aeiou" and len(vocal) == 1:
    # Convierte la vocal a mayúscula
    vocal_mayuscula = vocal.upper()

    # Reemplaza todas las ocurrencias de la vocal en la frase, tanto en mayúsculas como en minúsculas
    frase_modificada = ''
    for char in frase:
        if char.lower() == vocal.lower():
            frase_modificada += vocal_mayuscula
        else:
            frase_modificada += char

    # Muestra la frase modificada
    print("La frase con la vocal en mayúscula es:", frase_modificada)
else:
    print("Error: debes introducir una sola vocal.")

