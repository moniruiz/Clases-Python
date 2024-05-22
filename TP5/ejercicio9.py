#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y 
#muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también 
#funcione cuando el día o el mes se introduzcan con un solo carácter

fecha = input("Por favor, ingrese la fecha con el siguiente formato: dd/mm/aaaa ")

print("dia: " + fecha[:2])
print("mes: " + fecha[3:5])
print("año: " + fecha[6:])
