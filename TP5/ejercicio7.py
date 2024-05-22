#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por 
#pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con 
#dominio ceu.es

correo = input("Por favor, introduce tu correo electrónico: ")

divideCorreo = correo.split('@')

if len(divideCorreo) == 2:
    nuevo_correo = divideCorreo[0] + '@ceu.es'
    print("Tu nuevo correo es:", nuevo_correo)
else:
    print("Error: El correo electrónico proporcionado no es válido.")
