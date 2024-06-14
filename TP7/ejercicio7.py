#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que 
#ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

abecedario = list("abcdefghijklmnopqrstuvwxyz") 
print(abecedario)

lista_nueva =[]

for i, letra in enumerate(abecedario):
    if (i+1)%3 !=0:
        lista_nueva.append(letra)

print(lista_nueva)