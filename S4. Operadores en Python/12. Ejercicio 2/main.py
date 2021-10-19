numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero1 < numero2:
    print(f"{numero1} es menor que el numero {numero2}")
elif numero1 > numero2:
    print(f"{numero1} es mayor que el numero {numero2}")
else:
    print(f"{numero1} es igual que el numero {numero2}")