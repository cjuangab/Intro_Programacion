"""
Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. 
Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento del 10%. 
Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción a los jubilados. 
La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuentos). 
Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.

Para cada caso hacer:

● Una breve descripción de la situación comentada en la cabecera del archivo .py 
(similar a como hace Sergio en los ejemplos)

● Solución de pseudocódigo en PSeint

● Solución implementada en python en el mismo archivo donde se detalla la descripción
"""

print("---------------------------------------------------------")
print("-------------------     Bienvenido    -------------------")
print("---------------------------------------------------------")
print("")
cost = 1000
cant = int(input(" Ingrese la cantidad que desea adquirir el cliente: "))
print("¿Su cliente es Jubilado?")
jub = int(input("SI = 1 / NO = 0 "))
if(jub==1):
    if(cant >= 24):
        print(f"El costo total es: {cost*0.75*cant}")
    elif(cant >= 12):
        print(f"El costo total es: {cost*0.8*cant}")
    else:
        print(f"El costo total es: {cost*0.9*cant}")
else:
    if(cant >= 24):
        print(f"El costo total es: {cost*0.85*cant}")
    elif(cant >= 12):
        print(f"El costo total es: {cost*0.9*cant}")
    else:
        print(f"El costo total es: {cost*1*cant}")

print("---------------------------------------------------------")
print("---------------------------------------------------------")