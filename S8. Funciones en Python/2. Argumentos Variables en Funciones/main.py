def listarNombres(*nombres):  # De manera interna lo convierte a una tupla
    for nombre in nombres:    # Se conoce comunmente como *args en vez de *nombres
        print(nombre)


listarNombres("Juan", "Pedro", "Carla", "Maria", "Ernesto")
listarNombres("San", "Lorenzo")
