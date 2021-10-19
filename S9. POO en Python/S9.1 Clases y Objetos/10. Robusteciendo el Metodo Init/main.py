class Persona:
    def __init__(self, nombre, apellido, edad, *args, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrarDetalles(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad} {self.args} {self.kwargs}")


persona1 = Persona("Ricado", "Lopez", 62, '54912229942', 2, 3, 5, m="Manzana", p="Peras")  # Creacion de un objeto y asignacion de atributos
persona1.mostrarDetalles()

persona2 = Persona("Karla", "Gomez", 30)
persona2.mostrarDetalles()