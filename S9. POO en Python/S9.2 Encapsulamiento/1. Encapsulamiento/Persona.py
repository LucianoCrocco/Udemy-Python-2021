class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.__apellido = apellido
        self.edad = edad
    # El _ indica que no se tendria acceder a este atributo por fuera de nuestra clase
    # El __ es mas restrictivo, no es posible acceder al atributo directamente

    def mostrarDetalles(self):
        print(f"Persona: {self._nombre} {self.__apellido} {self.edad}")


persona1 = Persona("Ricado", "Lopez", 62)
persona1._nombre = "Juan Carlos"
persona1.__apellido = "Perez"
persona1.mostrarDetalles()