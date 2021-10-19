edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("Error... edad invalida.")
elif edad > -1 and edad < 11:
    print("La infancia es increible...")
elif edad > 9 and edad < 21:
    print("Muchos cambios y mucho estudio...")
elif edad > 19 and edad < 31:
    print("Amor y comienza el trabajo...")
else:
    print("Etapa de vida no reconocida")