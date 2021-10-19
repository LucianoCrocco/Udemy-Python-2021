class CalcularVolumenCubo:
    def __init__(self, ancho, alto, profundidad):
        self.ancho = altura
        self.alto = alto
        self.profundidad = profundidad

    def calcularVolumen(self):
        return self.ancho * self.alto * self.profundidad


ancho = int(input("Proporcione el ancho del cubo: "))
altura = int(input("Proporcione la altura del cubo: "))
profundidad = int(input("Proporcione la profundidad del cubo: "))

cubo = CalcularVolumenCubo(ancho, altura, profundidad)
print(f"El volumen del cubo con un acho de: {ancho}, altura {altura} y profundidad {profundidad} es: {cubo.calcularVolumen()}")