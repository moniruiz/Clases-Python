#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por 
#pantalla el número de veces que aparece la letra en la frase

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

if len(letra) != 1:
    print("Ingrese una sola letra")
else:
    contador = frase.count(letra)

print(f"La letra '{letra}' aparece {contador} veces en la frase ")