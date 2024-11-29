#Definir Clase Persona
class Persona:
    #Metodo Constructor de la clase persona
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    #Metodo o compartamiento saludar de la clase persona
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años"




