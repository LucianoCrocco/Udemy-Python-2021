# Definir una lista de tipo str
print("Definir una lista de tipo str")
nombres = ["Juan", "Karla", "Ricardo", "Maria"]

# Imprimir la lista de nombres
print("\n\tImprimir la lista de nombres")
print(nombres)

# Acceder a los elementos de una lista
print("\n\tAcceder a los elementos de una lista")
print(nombres[0])
print(nombres[1])

# Acceder a los elementos de manera inversa
print("\n\tAcceder a los elementos de manera inversa")
print(nombres[-1])
print(nombres[-2])

# Imprimir un rango
print("\n\tImprimir un rango")
print(nombres[0:2])  # Sin incluir el ultimo indice

# Ir del inicio de la lista al índice (sin incluirlo)
print("\n\tIr del inicio de la lista al índice (sin incluirlo)")
print(nombres[:3])  # Sin incluir el ultimo indice

# Desde el inidice indicado hasta el final
print("\n\tDesde el indice indicado hasta el final")
print(nombres[1:])  # Sin incluir el ultimo indice

# Cambiar un valor de la lista
print("\n\tCambiar un valor de la lista")
nombres[3] = "Ivone"
print(nombres)


# Iterar una lista
print("\n\tIterar una lista")
for i in nombres:
    print(i)
else:
    print("No existen mas nombres en la lista")

# Preguntar el largo de una lista
print("\n\tPreguntar el largo de una lista")
print(len(nombres))

# Agregar un elemento a la lista
print("\n\tAgregar un elemento a la lista")
nombres.append("Lorenzo")
print(nombres)

# Insertar un elemento a la lista en un indice especifico
print("\n\tAgregar un elemento a la lista")
nombres.insert(1, "Octavio")
print(nombres)

# Remover un elemento, no por indice sino por valor
print("\n\tRemover un elemento, no por indice sino por valor")
nombres.remove("Octavio")
print(nombres)

# Remover el ultimo valor agregado
print("\n\tRemover el ultimo valor agregado")
nombres.pop()
print(nombres)

# Remover un elemento en un indice indicado
print("\n\tRemover un elemento en un indice indicado")
del nombres[0]
print(nombres)

# Remover TODOS los elementos
print("\n\tRemover TODOS los elementos")
nombres.clear()
print(nombres)


# Borrar la lista de la memoria
print("\n\tBorrar la lista de la memoria")
del nombres
print(nombres)

