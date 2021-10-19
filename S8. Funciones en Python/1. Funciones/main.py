# Defincion y desarrollo de mi funcion

print("Defincion y desarrollo de mi funcion")


def miFuncion():
    print("Hola desde mi funcion")


# Llamada de mi funcion
miFuncion()

# Paso de argumentos
print("\nPaso de argumentos a una nueva funcion")


def nuevaFuncion(nombre, apellido):
    print(f"Nombre {nombre} - Apellido: {apellido}")


nuevaFuncion("Jose", "Perez")

# Funciones con retorno
print("\nFunciones con retorno")


def sumar(a, b):
    resultado = a + b
    return resultado


# resultado = sumar(9, 10)
# print(f"Resultado de la suma: {resultado}")

print(f"Resultado de la suma: {sumar(9, 10)}")

# Funciones con valores por default
print("\nFunciones con valores por default")


def restar(a=0, b=0) -> int:  # Indicio de cual es el tipo de dato que puede devolver la funcion
    return a - b              # Todos los tipos de datos en Python son dinamicos


print(f"Resultado de la resta: {restar()}")
