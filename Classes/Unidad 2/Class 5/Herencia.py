#Ejemplo de herencia tradicional
class Vehiculo:
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def descripcion(self):
        return f"Marca: {self.marca}; Modelo: {self.modelo}"


class Auto(Vehiculo):
    
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
    
    
    def descripcion(self):
        return f"Marca: {self.marca}; Modelo: {self.modelo}; Puertas: {self.puertas}"

automovil1 = Auto("Toyota", "Corolla", 4)
print(automovil1.descripcion())# Salida: Marca: Toyota; Modelo: Corolla; Puertas: 4