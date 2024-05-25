"""
Mostrar sólo los números pares desde 0 hasta el número ingresado (input).
Nota: para saber si un número es par hacer i % 2 == 0)
"""
print("------------------------")
print("Vamos a contar PARES")
print("------------------------")
i = 0
t = int(input("¿Hasta que numero queres contar? "))
while i <= t :
    if i % 2 == 0:
        print(i)
    i=i+1
    
print("------------------------")
print("")