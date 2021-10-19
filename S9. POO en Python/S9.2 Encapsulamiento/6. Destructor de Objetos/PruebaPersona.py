from Persona import Persona
# Le indico el archivo donde se encuentra mi clase, despues le indico que importe
# la clase que le pido, coincide que el archivo y la clase se llaman igual.
# Asi logramos importar clases desde otros archivos
# Si queremos importar todas las clases utlizamos el *

print(f"Creacion Objeto".center(30, "-"))
persona1 = Persona("Karla", "Gomez", 30)
persona1.mostrarDetalles()

print(f"Eliminacion de  Objeto".center(30, "_"))

del persona1

