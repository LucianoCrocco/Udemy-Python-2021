class Persona:
    def __init__(self):  # Con esta linea inicializo la clase (Es como un constructor). Agrego e inicializo atributos.
        self.nombre = "Juan"
        self.apellido = "Perez"
        self.edad = 28


# pass -> Unicamente sirve para declarar la funcion y no declarar contenido

persona1 = Persona()
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

# Una clase puede tener atributos y metodos
print(type(Persona))
