# En lugar de tener una coleccion de datos, pero organizadas a traves de una key
# Con la key podemos acceder al valor asociado al cual acceder.
# dict (key, value)
# Como con listas, tuplas y sets, cualquier tipo inmutable se puede utilizar
# int, float, bool, str, etc

# No existen los indices dentro de un diccionario, nuestra referencia es la key

diccionario = {
    "IDE": "Integrated Development Enviroment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Managment System"
}

print(diccionario)

# Saber la cantidad de elementos
print("\n\tSaber la cantidad de elementos")
print(len(diccionario))

# Acceder a un elemento
print("\n\tAcceder a un elemento")
print(diccionario["IDE"])

# Otra forma de acceder a un elemento
print("\n\tOtra forma de acceder a un elemento")
print(diccionario.get("OOP"))

# Modificar elementos
print("\n\tModificar elementos")
diccionario["IDE"] = "integrated development enviroment"
print(diccionario)

# Recorrer los elementos utilizando una funcion para recuperar la key:value
print("\n\tRecorrer los elementos utilizando una funcion para recuperar la key:value")
for termino, valor in diccionario.items():
    print(termino, valor)

# Recorrer los elementos recuperando solo la key
print("\n\tRecorrer los elementos recuperando solo la key")
for termino in diccionario.keys():
    print(termino)

# Recorrer los elementos recuperando el value
print("\n\tRecorrer los elementos recuperando el value")
for termino in diccionario.values():
    print(termino)

# Comprobar existencia de algun elemento
print("\n\tComprobar existencia de algun elemento")
print("IDE" in diccionario)
print("ASD" in diccionario)

# Agregar algun elemento, NO ES POSIBLE agregar llaves duplicadas, reemplaza el valor original
print("\n\tAgregar algun elemento, NO ES POSIBLE agregar llaves duplicadas, reemplaza el valor original")
diccionario["PK"] = "Primary Key"
print(diccionario)

# Remover un elemento
print("\n\tRemover un elemento")
diccionario.pop("DBMS")
print(diccionario)

# Remover TODOS los elemento
print("\n\tRemover TODOS los elemento")
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
print("\n\tEliminar el diccionario")
del diccionario
print(diccionario)
