#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario 
#lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de 
#usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

nombre = input("Por favor, introduce tu nombre: ")

nombreSinEspacio = nombre.strip()

nombreMayusculas = nombreSinEspacio.upper()

cantidadDeLetras = len(nombreSinEspacio)

print(f"{nombreMayusculas} tiene {cantidadDeLetras} letras")
