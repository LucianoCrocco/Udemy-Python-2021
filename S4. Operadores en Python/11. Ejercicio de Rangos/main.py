edad = int(input("Ingrese su edad: "))

minimo = 20
maximo = 39

if edad <= maximo and edad >= minimo:
    print(f"Se encuentra entre el rango etario de {minimo} y {maximo+1}")
    if edad < 31:
        print(f"Se encuentra en el rango de los 20's")
    else:
        print(f"Se encuentra en el rango de los 30's")
else:
    print(f"NO se encuentra entre el rango etario de {minimo} y {maximo+1}")