# Dada la siguiente tupla, crear una lista que sólo incluya los números menor que 5
# utilizando un ciclo for: tupla = (13, 1, 8, 3, 2, 5, 8)

miTupla = (13, 1, 8, 3, 2, 5, 8)

print(f"Tupla antes del for: {miTupla}")
miLista = []

for i in range(len(miTupla)):
    if miTupla[i] < 5:
        miLista.append(miTupla[i])
    else:
        print(f"{miTupla[i]} es mayor a 5")

miTupla = tuple(miLista)
print(f"Tupla despues del for: {miTupla}")