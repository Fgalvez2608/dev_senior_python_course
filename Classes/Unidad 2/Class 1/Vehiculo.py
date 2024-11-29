# Uso de herencia

# Clase padre Vehiculo
class Vehiculo:
    # Constructor de la clase Vehiculo 
    def __init__(self, tipo):
        self.tipo = tipo
    
    # Metodo de la clase Vehiculo
    def descripcion(self):
        return f"Este vehiculo es de tipo: {self.tipo}"

#clase hijo de la clase Vehiculo Moto que hereda de la clase Vehiculo
class Moto(Vehiculo):
    
    # Constructor de la clase Moto
    def __init__(self, tipo, marca):
        super().__init__(tipo) # heredo con la funcion super()
        self.marca = marca

#creacion de objeto
moto = Moto("Motocicleta", "Ducatti")
print(moto.descripcion())