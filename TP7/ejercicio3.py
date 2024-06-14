#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
#Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada 
#asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado 
#<nota> donde <asignatura> es cada una de las asignaturas de la lista y <nota> cada una de las 
#correspondientes notas introducidas por el usuario.

asignaturas =  ["Matemáticas"," Física" , "Quimica" , "Historia", "Lengua"]

notas ={}

for asignatura in asignaturas:
    nota = input(f"Que nota has sacado en {asignatura}?: ")
    notas[asignatura]= nota

for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}")