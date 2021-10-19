print(f"\tCiclo for\n")

cadena = "Hola"

for i in cadena:
    print(i)
else:
    print("Fin ciclo for")

print(f"\n\tCiclo for con break")
for i in "Holanda":
    if i == 'a':
        print(f"Palabra encontrada: {i}")
        break
else:
    print(f"No se encontro la letra 'a' {i}")


print(f"\n\tCiclo for con continue")
for i in range(6):
    if i % 2 != 0:
        print(f"Valor: {i}")
        continue
    else:
        print(f"{i} no es numero par")
