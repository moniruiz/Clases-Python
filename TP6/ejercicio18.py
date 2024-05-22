#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al 
#usuario por la contraseña hasta que introduzca la contraseña correcta

cadena = "contraseña"

while True:
    password = input("Ingrese la contraseña: ")
    #nueva_contraseña = password.lower()

    if password == cadena:
        print("La contraseña es correcta")
        break
    else:
        print("La contraseña es incorrecta, intente nuevamente")