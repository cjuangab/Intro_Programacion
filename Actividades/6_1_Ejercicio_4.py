"""
En una escuela, luego de tomar un determinado examen, 
es necesario calcular el promedio de notas (las notas van de 0 a 10)
de los alumnos de un curso.
Se necesita saber si el rendimiento ha sido elevado (el promedio es mayor a 8),
aceptable (el promedio está comprendido entre 6 y 8) o bajo (promedio es inferior a 6). 
Desarrollar un algoritmo que resuelva este problema. 
Para tener en cuenta: las autoridades del colegio saben cuántos estudiantes del curso
han rendido el examen.
"""
##Condiciones iniciales
nota = 0

print("------------------------")
print("Rendimiento de alumnos")
print("------------------------")
## Captura de datos
est = int(input("Ingrese la cantidad de estudiantes que rindieron el examen: "))
while est <= 0:
    est = int(input("Ingrese un valor valido: "))
for i in range(0,est):
    aux =  int(input(f"Ingrese el valor de la calificacion del estudiante N°{i+1}: "))
    while not((aux>0)&(aux<11)):
        aux=int(input("Ingrese una Calificaicon valida: "))
    nota = nota + aux
            
## Procesamiento de datos
nota = nota/est
if nota < 6:
    print("El rendimiento es del curso es bajo")
    print(f"El promedio de notas es {nota}")
elif nota<=8:
    print("El rendimiento del curso es aceptable")
    print(f"El promedio de notas es {nota}")
else:
    print("El rendimiento del curso es Alto")
    print(f"El promedio de notas es {nota}")
    
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")