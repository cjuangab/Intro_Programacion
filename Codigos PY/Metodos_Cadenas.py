# Una cadena es un conjunto de caracteres 
# Es un tipo de "Variable" mas compleja que llamamos Objeto
# esta entre comillas el "variable" ya que siendo riguroso no lo es
# Se escribe justamente entre "" a las cadenas ej: "Hola Mundo"

nombre = "cadena" 
# Creo una cadena con el nombre de la cadena y asignando
# entre "" el valor de la cadena               

#EJ:
alumno = "Juan Carlos"

# METODOS
# son operaciones que pueden realizar las cadenas
# los metodos siguen la sintaxis de nombre_cadena.Metodo()
# exepto el dir() que no es un metodo sino una funcion

print(dir(nombre_cadena)) #nos devuelve un listado de los metodos que puede realizar


.upper() #Convierte todo a mayusculas
alumno.upper() #devuelve "JUAN CARLOS"

.lower() #Convierte todo a minusculas
alumno.lower() #devuelve "juan carlos"

.capitalize() #Convierte la primera letra a Mayuscula
alumno.capitalize() #devuelve "Juan carlos"

.find("elemento_a_buscar") #Nos devuelve la posicion en la cual encotro al elemento
alumno.find("Carlos") #devuelve 5
alumno.find("Hola") #devuelve -1 porque no lo encontro
alumno.find("o") #devuelve 9

.index("elemento_a_buscar") #Funciona igual que find solo que si no encuentra el
#valor lanza una excepcion
alumno.index("Carlos") #devuelve 5
alumno.index("Hola") #devuelve una excepcion porque no lo encontro
alumno.index("o") #devuelve 9

.isnumeric() #Consulta si es numerico y devuelve True o False
alumno.isnumeric() #devuelve False

.isalpha() #Consulta si es alfanumerico y devuelve True o False
alumno.isalpha() #devuelve False porque los espacios no son alfanumericos, son especiales

.count("elemento_a_buscar") #Cuenta la cantidad de veces que encuentra una coincidencia
alumno.count("Juan") #devuelve 1
alumno.count("a") #devuelve 2
alumno.count("x") #devuelve 0

len(cadena) #Cuenta los caracteres, NO es un metodo, es una FUNCION
len(alumno) #devuelve 10
len("Pablo_4") #devuelve 7

.startswith("a_consultar") #Consulta si la cadena empieza con "..."
alumno.startswith("Ju") #devuelve True
alumno.startswith("j") #devuelve False
alumno.startswith("Hola") #devuevle False
alumno.startswith("Juan") #devuelve True

.endswith("a_consultar") #Consulta si la cadena termina con "..."
alumno.endswithswith("Ju") #devuelve false
alumno.endswithswith("s") #devuelve True
alumno.endswithswith("Hola") #devuevle False
alumno.endswithswith("Carlos") #devuelve True

.remplace("original","remplazo") #Remplaza en la cadena origial
# por un valor que nosotros le ingresemos
alumno.replace("Juan","Pablo") #devuelve "Pablo Carlos"
alumno.replace("a","Hola") #devuelve "JHolaan CHolarlos" remplazo las a por Hola

.split("elemento_referencia") #Crea una lista separando los elementos en base
#al elemento de refencia que le ingresemos
alumno.split(" ") #devuelve [Juan,Carlos]
alumno.split("a") #devuelve [Ju,n C,rlos]
