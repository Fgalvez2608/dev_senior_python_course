# Clase Animall
class Animall:
    
    cantidadAnimales = 0
    
    # Constructor de la clase
    def __init__(self, name):
        self.name = name
        Animall.cantidadAnimales += 1 #incrementar la cantidad de animales

# Decorador
    @classmethod
    def totalAnimales(cls):
        return f"Tengo {cls.cantidadAnimales} animales"

# Crear objetos
animal1 = Animall("Ares")
animal2 = Animall("Arya")
animal3 = Animall("Zeus")
animal4 = Animall("Hades")

# Acceder 
print(Animall.cantidadAnimales)
print(animal3.name)
print(Animall.totalAnimales())




