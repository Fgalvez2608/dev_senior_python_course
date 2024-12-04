class Animal:
    
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "Todo animal habla de alguna forma"

    def __str__(self):
        return f"El animal se llama {self.nombre}"

class Perro(Animal):
    
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hablar(self):
        return "El perro dice: Guau guau"

    def __str__(self):
        return f"El nombre del perro {self.nombre} y su raza es {self.raza}"


animal1 = Animal("Ares")
perro1 = Perro("Arya", "Bulldog Frances")
print(animal1.hablar())
print(animal1.__str__())
print(perro1.hablar())
print(perro1.__str__())