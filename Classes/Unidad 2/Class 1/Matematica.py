# Metodos estaticos

# Clase matematica
class Matematica:
    
    #decorador static
    @staticmethod
    def suma(a, b):
        return a + b
    
    @staticmethod
    def resta(a, b):
        return a - b

print(Matematica.suma(10, 20))
print(Matematica.resta(10, 20))