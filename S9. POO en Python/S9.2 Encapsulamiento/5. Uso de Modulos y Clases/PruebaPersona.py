from Persona import Persona
# Le indico el archivo donde se encuentra mi clase, despues le indico que importe
# la clase que le pido, coincide que el archivo y la clase se llaman igual.
# Asi logramos importar clases desde otros archivos
# Si queremos importar todas las clases utlizamos el *


persona1 = Persona("Karla", "Gomez", 30)
persona1.mostrarDetalles()

# Nos muestra el nombre del modulo que se esta ejecutando, en el caso de PruebaPersona es el modulo principal
print(__name__)