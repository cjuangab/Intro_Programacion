#Listas

lista = [elemento 1 , elemento 2 , elemento 3 ,elemento n... ]
# Los elementos se guardan en indices que arrancan desde el 0 para el elemento 1, se pueden modificar
# Se crean y se llama con []
lista[n_indice] = #modificar un elemento en el indice x
lista[n_indice] # Me devuelve el elemento guardado en el indice x
#EJ:
datos_personales = ["Marcos","Fernandez", 29, True] #Creo Una lista
print(datos_personales[2]) # Me imprime el elemento en el indice 2 osea tercer elemento de la lista (29)
print(datos_personales) # Imprime lista completa
datos_personales[3]=False #Modifico el cuarto elemento de la lista, el ubicado en el indice 3

len(cadena) #Cuenta los elementos, NO es un metodo, es una FUNCION
len(datos_personales) #devuelve 4


#METODOS DE LISTAS
# son operaciones que pueden realizar las listas
# los metodos siguen la sintaxis de nombre_lista.metodo()
# exepto el dir() que no es un metodo sino una funcion

.append(...) #Agrega un elemento a la lista al final
datos_personales.append("Soltero") #Agrega a la lista el elemento soltero
# la lista quedaria ["Marcos","Fernandez", 29, True, "Soltero"]

.insert(n_indice,elemento) #Agrega un elemento en el indice ingresado
#conservando y desplazando el resto
datos_personales.insert(2,"Soltero") #La lista quedaria ["Marcos","Fernandez", "Soltero", 29, True]

.extend([lista]) #Agrega una lista al final de la lista original
datos_personales.extend(["Casado",2,False]) #La lista quedaria
# ["Marcos","Fernandez", 29, True,"Casado",2,False]

.pop(indice) #Elimina el elemento del indice indicado desplazando hacia la izquierda
# en caso de no indicarle un indice o colocar -1 elimina el ultimo elemento de la lista
datos_personales.pop(1) #La lista quedaria ["Marcos", 29, True]
datos_personales.pop() #La lista quedaria ["Marcos","Fernandez", 29]

.remove(elemento) #Busca y elimina el elemento que le ingresemos en la lista
# En caso de no existir lanza una excepcion
datos_personales.remove("Fernandez") #La nueva lista quedaria ["Marcos", 29, True]

.clear() #Limpia la lista, la deja vacia
datos_personales.clear() #La nueva lista quedaria []

.sort() #Ordena la lista de menor a mayor, o alfabeticamente ascendente
# pero requiere que todos los datos sean del mismo tipo: sean cadenas o valores numericos
.sort(reverse=1) o (reverse=True) #Ordena la lista de mayor a menor, o alfabeticamente descendente
# pero requiere que todos los datos sean del mismo tipo: sean cadenas o valores numericos

.reverse() #Invierte el orden de los elementos de cualquier tipo de lista
#no los ordena, solo invierte las posiciones
datos_personales.reverse() #La lista quedaria [True,29, "Fernandez", "Marcos"]

.index(elemento) #Busca y nos devuelve el indice donde se encuentra el elemento 
datos_personales.index(True) #Nos devuelve 3


#TUPLA

tupla = (elemento 1 , elemento 2 , elemento 3 ,elemento n... )
# Un tipo de arreglo que no se puede modificar, pero puedo acceder por n de indice a cada elemento
# Se crea con () pero se llama con []

tupla[n_indice] # Me devuelve el elemento guardado en el indice x
#EJ:
datos_personales = ("Marcos","Fernandez", 29, True) #Creo Una tupla
print(datos_personales[2]) # Me imprime el elemento en el indice 2 osea tercer elemento de la tupla (29)
print(datos_personales) # Imprime tupla completa


#CONJUNTO

conjunto = {elemento 1 , elemento 2 , elemento 3 ,elemento n... }
# Un tipo de arreglo que no se puede modificar los elementos pero si el orden de los mismos
# No se puede acceder a los elementos por numero de indice
datos_personales = {"Marcos","Fernandez", 29, True} #Creo Un conjunto
print(datos_personales) # Imprime conjunto complet

#DICCIONARIO

diccionario = {
    'nombre_elemento1' : elemento 1,
    'nombre_elemento2' : elemento 2,
    'nombre_elemento3' : elemento 3,
    'nombre_elementon' : elemento n,
}

# Un arreglo al que se puede acceder por su clave
# diccionario['clave_elemento...']

datos_personales = {     #Creo un diccionario
    'nombre' : "Marcos",  #Cada elemento define su clave de elemento entre ''
    'apellido' : "Fernandez", # : el elemento a guardar
    'edad' : 29,    # cerrando cada fila con , como la separacion de cada elemento en una lista
    'estado' : True  # el ultimo elemento no cierra con , 
}

print(datos_personales) #imprime el diccionario completo
print(datos_personales['edad']) # Imprime el dato almacenado en dicha clave

#METODOS DE Diccionarios
# son operaciones que pueden realizar los diccionarios
# los metodos siguen la sintaxis de nombre_diccionario.metodo()
# exepto el dir() que no es un metodo sino una funcion

.keys() #Devuelve las claves del diccionario
datos_personales.keys() #Nos devolveria ['nombre', 'apellido', 'edad', estado]

.get('key') #Devuelve el valor alojado en la clave correspondiente
datos_personales.get('nombre') #Nos devolveria "Marcos"

.clear() #Elimina todos los elementos del diccionario
datos_personales.clear() #Nos devolveria {}

.pop('key') #Elimina el elemento ubicado en la clave ingresada
datos_personales.pop('nombre') #Nos devuelve {'apellido': "Fernandez", 'edad': 29, 'estado': True}
.pop('key1','key2','keyn') #Me permite eliminar mas de un elemento

.items() #Nos devuelve una lista de elementos conformados por tuplas de pares
#[('key1':elemento),('key2':elemento),...,('keyn':elemento_n)]
datos_personales.items() #Nos devuelve la lista:
# [('nombre', 'Marcos'), ('apellido', 'Fernandez'), ('edad', 29), ('estado', True)]


