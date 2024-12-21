# Ejemplo de composicion 1
class Vehiculo:

    def __init__(self, motor):
        self.motor = motor
    
    def encender(self):
        print("Encendiendo el Vehiculo:")
        self.motor.iniciar()

class Motor:

    def __init__(self):
        pass

    def iniciar(self):
        pass

class MotorGasolina(Motor):

    def __init__(self):
        pass

    def iniciar(self):
        print("Motor Gasolina encendido")

class MotorElectrico(Motor):

    def __init__(self):
        pass

    def iniciar(self):
        print("Motor Electrico encendido")

motorGasolina = MotorGasolina() 
motorElectrico = MotorElectrico()

autoGasolina = Vehiculo(motorGasolina)
autoElectrico = Vehiculo(motorElectrico)

autoGasolina.encender()
autoElectrico.encender()

