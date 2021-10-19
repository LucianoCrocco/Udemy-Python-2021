class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Un decorador se encarga de modificar el comportamiento de nuestro metodo
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def mostrarDetalles(self):
        print(f"Persona: {self._nombre} {self.apellido} {self.edad}")


persona1 = Persona("Ricardo", "Lopez", 62)
print(persona1.nombre)

persona1.nombre = "Juan Carlos"
print(persona1.nombre)