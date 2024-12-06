#clases abstractas y metodos abstractos
from abc import ABC, abstractmethod # importa los metodos abstractos para definir una clase abstracta

class Forma(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Circulo(Forma):

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return f"El area del circulo es: {3.1416 * self.radio * self.radio}"

    def perimetro(self):
        return f"El perimetro del circulo es: {2 * 3.1416 * self.radio}"

class Rectangulo(Forma):
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return f"El area del rectangulo es: {self.base * self.altura}"

    def perimetro(self):
        return f"El perimetro del rectangulo es: {2 * (self.base + self.altura)}"

    def diagonal(self):
        return f"La diagonal del rectangulo es: {self.base * self.base + self.altura * self.altura}"

class Cuadrado(Forma):

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return f"El area del cuadrado es: {self.lado * self.lado}"



formas = [
    Circulo(26),
    Rectangulo(12, 22),
    Cuadrado(18)
]

print("Area de las formas")
for forma in formas:
    print(forma.area())

print("")
circulo1 = Circulo(26)
print(circulo1.perimetro())

print("")
rectangulo1 = Rectangulo(12, 22)
print(rectangulo1.diagonal())











