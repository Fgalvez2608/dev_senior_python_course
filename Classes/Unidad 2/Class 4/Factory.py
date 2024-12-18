# Patron de diseno Factory

from abc import ABC, abstractmethod

#Clase abstracta
class Clases(ABC): # clase padre o super clase
    @abstractmethod
    def operacion(self):
        pass

class ClaseA(Clases): #clase hija o subclase
    def operacion(self):
        return "Esta es la clase A"

class ClaseB(Clases): #clase hija o subclase
    def operacion(self):
        return "Esta es la clase B"

    def impresion(self):
        pass

    def consultar(self):
        pass

    def retiro(self):
        pass


#Clase Factory
class FabricaDeClases:
    
    @staticmethod
    def creacionObjetos(tipoObjeto):
        if tipoObjeto == "A":
            return ClaseA()
        elif tipoObjeto == "B":
            return ClaseB()
        else:
            raise ValueError(f"La clase {tipoObjeto} no existe") #Gestion de errores

objeto1 = FabricaDeClases.creacionObjetos("A")
objeto2 = FabricaDeClases.creacionObjetos("B")
#objeto3 = FabricaDeClases.creacionObjetos("C")

print(objeto1.operacion())
print(objeto2.operacion())
print(objeto2.retiro())
#print(objeto3.operacion())



