def desplegarNombres(nombres):
    for i in nombres:
        print(i)


nombresLista = ["Juan", "Carla", "Guillermo"]
desplegarNombres(nombresLista)
nombresTupla = ("Pedro", "Jorge", "Camilo")
desplegarNombres(nombresTupla)
nombresSet = {"Ricardo", "Julio", "Alejandro"}
desplegarNombres(nombresSet)

desplegarNombres("Carlos")  # Itera los caracteres
desplegarNombres((10, 11))  # Como tupla
desplegarNombres([9, 1])  # Como lista
desplegarNombres({77, 99})  # Como set