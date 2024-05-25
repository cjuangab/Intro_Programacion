"""
Un profesor de matemática necesita generar la tabla de multiplicar de un número entero 
comprendido entre 1 y 10. Por ejemplo para el 3 debería aparecer como salida:
3x1=3
3x2=6
3x3=9
…. y así hasta 10
5.2 Resuelva este problema utilizando un para y 
de modo que por la salida se emita la tabla tal como se propone.
"""

print("------------------------")
print("Tabla de multiplicar")
print("------------------------")

x=int(input("De que numero desea conocer la tabla: "))
print("------------------------")
print(f"Okey aqui vamos con la tabla del {x}")
print("------------------------")
for i in range(1,11):
    print(f"{x} X {i} = {x*i}")
    
print("------------------------")
print("------------------------")