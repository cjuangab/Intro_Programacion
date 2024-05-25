# Son operadores que responden a las funciones logicas con sus mismos nombres
# Respetan las tablas de verdad de las mismas


# AND   &
# Requiere que todas las sentencias sean verdaderas
# para devolver Verdadero

True & True  # Devuelve True
True & False  # Devuelve False
False & True  # Devuelve False
False & False  # Devuelve False

# OR |
# Requiere que al menos una de las sentencias sea verdadera
# para devolver un Verdadero

True | True  # Devuelve True
True | False  # Devuelve True
False | True  # Devuelve True
False | False  # Devuelve False

# NOT  not
# Niega cualquier sentencia

not True # Devuelve False
not False # Devuelve True
not (True & False) # Niega el False del and y devuelve True
not (True | False) # Niega el True del or y devuelve False