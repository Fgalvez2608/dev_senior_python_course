# clase Banco
class Banco:
    
    TASA_INTERES = 0.03 #constante de clase
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    @classmethod
    def cambiarTasa(cls, nuevaTasa):
        cls.TASA_INTERES = nuevaTasa
    
    @staticmethod
    def conversionDolaresEuros(dolares):
        return dolares * 0.85
    
banco1 = Banco("BANCOLOMBIA")
print(banco1.nombre)

banco2 = Banco("BANCO DE BOGOTA")
print(banco2.nombre)

banco3 = Banco("BANCO DE CALI")
print(banco3.nombre)

banco1.cambiarTasa(0.05)
print("La tasa de interes del banco 1 es de: ", Banco.TASA_INTERES)

