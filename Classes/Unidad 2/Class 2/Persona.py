class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad
        self.__cuentaBancaria = 123456

    def mostrarInformacion(self):
        return f"Nombre: {self.nombre}; Edad: {self._edad}"

    def __mostrarCuenta(self):
        return f"Cuenta Bancaria: {self.__cuentaBancaria}"

    def mostrarInforrmacionCompleta(self):
        return f"{self.mostrarInformacion()}, {self.__mostrarCuenta()}"

persona1 = Persona("FGALVEZ", 33)
print (persona1.nombre)
print (persona1._edad)
print (persona1.mostrarInformacion())
print (persona1.mostrarInforrmacionCompleta())
