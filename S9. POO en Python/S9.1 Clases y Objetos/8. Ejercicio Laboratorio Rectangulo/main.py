class AreaRectangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcularArea(self):
        return self.base * self.altura


altura = int(input("Proporcione la altura: "))
base = int(input("Proporcione la base: "))

area = AreaRectangulo(altura, base)
print(f"El area de del rectangulo con altura {altura} y base {base} es: {area.calcularArea()}")