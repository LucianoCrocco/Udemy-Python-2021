# Función input para procesar la entrada de datos del usuario
resultado = input("Escriba un mensaje: ")
print("Valor proporcionado:", resultado)
# La funcion input pide un string, vamos a tener que castear y validar posteriormente nuestro dato

numero1 = int(input("\nIngrese el primer numero: ")) # Casteo mi funcion input
numero2 = int(input("Ingrese el primer segundo: "))

resultado = numero1 + numero2
print("El resultado de la suma es:", resultado)

print("Fin del programa")
