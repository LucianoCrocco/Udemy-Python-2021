# Una clase contiene atributos pero tambien posee metodos.
# Los atributos son las caracteristicas que van a tener nuestros objetos al momento de crearlos a partir de una clase.
# Los metodos son el comportamiento de nuestros objetos.

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrarDetalle(self):  # Se lo conoce como metodo de instancia xq se va a asociar con los objetos que vamos a crear.
        print(f"Objeto Persona: {self.nombre} {self.apellido} {self.edad}")


persona1 = Persona("Ricado", "Lopez", 62)
Persona.mostrarDetalle(persona1)

persona2 = Persona("Karla", "Gomez", 30)
Persona.mostrarDetalle(persona2)
