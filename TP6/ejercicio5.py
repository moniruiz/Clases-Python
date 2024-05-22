#Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales 
#o superiores a $ 450.000 mensuales. Escribir un programa que pregunte al usuario su edad y sus 
#ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no

edad = int(input("Por favor, ingrese su edad: "))
ingresos = float(input("Por favor, ingrese su monto mensual: "))

edad_minima = 18
ingresos_minimo = 450000

if edad >=edad_minima and ingresos_minimo >= ingresos:
    print("Usted puede tributar porque cumple con los requisitos")
else:
    if edad < edad_minima and ingresos_minimo < ingresos:
        print("Usted no puede tributar porque no cumple con los requisitos minimos")
    elif edad < edad_minima:
        print("usted no puede tributar porque no es mayor de edad")
    elif ingresos < ingresos_minimo:
        print("Usted no puede tributar porque no cumple ")


