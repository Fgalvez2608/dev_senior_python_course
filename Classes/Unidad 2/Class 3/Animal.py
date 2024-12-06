class Animal:

    def __init__(self):
        pass

    def hablar(self):
        pass

class Perro(Animal):
    
    def __init__(self):
        super().__init__()
        pass

    def hablar(self):
        return "El perro dice: Guau guau"

class Gato(Animal):
    
    def __init__(self):
        super().__init__()
        pass

    def hablar(self):
        return "El gato dice: Miau miau"

animales = [
    Perro(),
    Gato(),
    Gato(),
    Perro()
]

for animal in animales:
    print(animal.hablar())










