# Una clase contiene atributos pero tambien posee metodos.
# Los atributos son las caracteristicas que van a tener nuestros objetos al momento de crearlos a partir de una clase.
# Los metodos son el comportamiento de nuestros objetos.
# El operador self en Python es conocido en otros lenguajes como this

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrarDetalle(this):  # Se lo conoce como metodo de instancia xq se va a asociar con los objetos que vamos a crear.
        print(f"Objeto Persona: {this.nombre} {this.apellido} {this.edad}")


persona1 = Persona("Ricado", "Lopez", 62)
# Persona.mostrarDetalle(persona1)
# Otra manera de mostrar persona1:
# Podemos agregar atributos a nuestro objeto a pesar que no esten definidos en nuestra clase
# Sin embargo estos atributos no se van a compartir con los demas objetos. Es decir, es local al objeto que se lo agrego.
persona1.telefono = 54913330939
persona1.mostrarDetalle()
print(f"Objeto Persona 1 telefono, agregandole un atributo al vuelo : {persona1.telefono}")


persona2 = Persona("Karla", "Gomez", 30)
Persona.mostrarDetalle(persona2)
