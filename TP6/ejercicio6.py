#Los impuestos de la DRG para la declaración de un alquiler son los siguientes:
#Alquiler               Tipo impositivo
#Menos de $ 100.000             5%
#Entre $ 100.000 y $ 200.000    15%
#Entre $ 200.000 y $ 350.000    20%
#Entre $ 350.000 y $ 600.000    30%
#Más de $ 600.000               45%
#Escribir un programa que pregunte al usuario su alquiler y muestre por pantalla el tipo impositivo 
#que le corresponde con su cálculo correspondiente.

alquiler = float(input("Por favor, ingrese el monto de su alquiler: "))

if alquiler < 100000:
    tipo_impositivo = 5
elif alquiler > 100000 and alquiler <= 200000:
    tipo_impositivo = 15
elif alquiler > 200000 and alquiler <= 350000:
    tipo_impositivo = 20
elif alquiler > 350000 and alquiler <= 600000:
    tipo_impositivo = 30
else:
    tipo_impositivo = 45

impuesto = alquiler * (tipo_impositivo / 100)

print(f"Para un alquiler de ${alquiler:.2f}, el tipo impositivo aplicable es del {tipo_impositivo}%.")
print(f"El impuesto a pagar es de: ${impuesto:.2f}")
