"""
Pedir que el usuario ingrese (input) nombre de personas 
y mostrarlos hasta que el valor de lo que ingresa sea “fin”
"""
print("------------------------")
nomb = input("Ingrese el nombre: ")
while (nomb != "fin") & (nomb != "Fin"):
    print(f"El nombre ingresado es: {nomb}")
    nomb = input("Ingrese el nombre: ")

print("------------------------")
print("Hasta Pronto")
print("------------------------")