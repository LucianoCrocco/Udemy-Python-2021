mes = int(input("Ingeese el mes del año (1-12): "))
estacion = None

if mes >= 1 and mes <=3:
    estacion = "Verano"
elif mes >= 4 and mes <= 6:
    estacion = "Otoño"
elif mes >= 7 and mes <= 9:
    estacion = "Invierno"
else:
    estacion = "Primavera"

print(f"Estacion: {estacion}")