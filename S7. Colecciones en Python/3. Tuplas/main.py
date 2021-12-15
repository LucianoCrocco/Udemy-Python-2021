# La listas son mutables, a diferencia de las listas, las Tuplas NO SON modificables, es inmutable.
# Son similares a las listas pero la diferencia principal es la anteriormente mencionada.

frutas = ("Naranja", "Platano", "Guayaba")
print(frutas)

# Saber el largo (cantidad de elementos)
print("\n\tSaber el largo (cantidad de elementos)")
print(len(frutas))


# Acceder a un elemento
print("\n\tAcceder a un elemento")
print(frutas[1])

# Navegacion inversa
print("\n\tNavegacion inversa")
print(frutas[-1])


# Acceder aun rango de valores
print("\n\tAcceder aun rango de valores")
print(frutas[0:1])
print("La coma al final de la tupla al mostrar un rango 0:1 hace la diferencia entre un string y una tupla")

# Recorrer elementos
print("\n\tRecorrer elementos y modificar el ultimo caracter que lee")
for fruta in frutas:
    print(fruta, end=' ')

# Cambiar el valor de una tupla
# frutas[0] = 'Pera' -> No funciona
# Para hacerlo creamos una lista y le asignamos la tupla, cambiamos la lista y volvemos a asignar a la tupla
print("\n\n\tCambiar el valor de una tupla")
frutaLista = list(frutas)
frutaLista[0] = 'Pera'
frutas = tuple(frutaLista)
print(frutas)

# Eliminar la tupla por completo
print("\n\tEliminar la tupla por completo -> del frutas")
del frutas
print(frutas)