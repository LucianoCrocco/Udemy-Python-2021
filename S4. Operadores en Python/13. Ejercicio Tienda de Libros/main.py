print("\t\t[Proporcione los siguientes datos del libro]\n")
nombre = str(input("Ingrese el nombre: "))
idLibro = int(input("Ingrese el ID: "))
precio = float(input("Ingrese el precio: "))
envio = bool(input("Indique si el envio es gratuito (True/False): "))

print(f"\tNombre: {nombre}"
      f"\tID: {idLibro}"
      f"\tPrecio: {precio}"
      f"\tEnvio: {envio}")