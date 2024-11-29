# Clase Animal
class Animal:
    
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # Metodos
    def saludar(self):
        return f"Mi animal se llama {self.name} y tiene {self.age} años"

# crear objetos
animal1 = Animal("Ares", 3)

# acceder a los atributos
print(animal1.name) #Accedo al nombre del animal
print(animal1.age) #Accedo a la edad del animal

# acceder a los metodos
print(animal1.saludar()) #Accedo al metodo saludar