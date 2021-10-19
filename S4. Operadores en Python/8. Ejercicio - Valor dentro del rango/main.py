minimo = 0
maximo = 5
numero = int(input(f"Ingrese un numero dentro del rango {minimo} y {maximo}: "))

if numero <= maximo and numero >= minimo:
    print(f"El numero ingresado ({numero}) esta dentro del rango")
else:
    print(f"El numero ingresado ({numero}) NO esta dentro del rango")