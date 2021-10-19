class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrarDetalles(self):
        print(f"Persona: {self._nombre} {self.apellido} {self.edad}")


# Si queremos que solo se ejecute nuestro main podemos utilizar el siguiente codigo.

if __name__ == "__main__":
    persona1 = Persona("Ricardo", "Lopez", 62)
    persona1.mostrarDetalles()

    persona1.nombre = "Juan Carlos"
    print(persona1.nombre)

    persona1.apellido = "Messi"
    print(persona1.apellido)

    persona1.edad = 33
    print(persona1.edad)

# Nos muestra el nombre del modulo que se esta ejecutando, en el caso de PruebaPersona es el modulo principal
print(__name__)