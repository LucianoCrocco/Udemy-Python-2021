# Un set no mantiene un orden (no existe un indice), no tiene elementos duplicados
# No es posible modificar los elementos almacenados, pero si eliminar o agregar

planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

# Conocer la cantida de elementos
print("\n\tConocer la cantida de elementos")
print(len(planetas))

# Revisar si un elemento esta presente
print("\n\tRevisar si un elemento esta presente, tambien utilizable en listas y tuplas")
print("Marte" in planetas)

# Agregar mas elementos
print("\n\tAgregar mas elementos")
planetas.add("Tierra")
print(planetas)

# No se pueden duplicar elementos
print("\n\tNo se pueden duplicar elementos, intentamos nuevamente agregar Tierra")
planetas.add("Tierra")
print(planetas)

# Eliminar elemento, si no lo encuentra devuelve error
print("\n\tEliminar elemento, si no lo encuentra devuelve error")
planetas.remove("Tierra")
print(planetas)

# Eliminar elemento, si no lo encuentra NO devuelve error
print("\n\tEliminar elemento, si no lo encuentra NO devuelve error")
planetas.discard("Tierra")
print(planetas)

# Limpiar todos los elementos de un set
print("\n\tLimpiar todos los elementos de un set")
planetas.clear()
print(planetas)

# Eliminar nuestro set
print("\n\tEliminar nuestro set")
del planetas
print(planetas)




