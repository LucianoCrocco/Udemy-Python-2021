# Cadena (String)
miGrupoFavorito: str = "Aerosmith" + " The best rock band"
comentario: str = ", better than yours"
print("Mi grupo favorito es: " + miGrupoFavorito + comentario)

print("Mi grupo favorito es:", miGrupoFavorito, comentario)  # Con la coma agrega un espacio en blanco y concatenta

numero1 = "1"
numero2 = "2"
print(numero1 + numero2)  # No suma, se concatena.

numero1 = 1
numero2 = 2
print(numero1 + numero2)  # Ahora si se suma

numero1 = "1"
numero2 = "2"
print("Concatenacion:", numero1 + numero2)  # Casteo. Para castear tiene que ser un valor valido "1" != "uno"
print("Suma casteando el dato:",  int(numero1) + int(numero2))  # Casteo.
