class CuentaBancaria:
    
    def __init__(self, titular, saldo, password):
        self.titular = titular
        self._saldo = saldo
        self.__password = password

    def depositar(self, cantidadDeposito):
        self._saldo += cantidadDeposito
        return f"Deposito Existoso!!!, Saldo Actual: {self._saldo}"

    def retirar(self, cantidadRetiro):
        if (cantidadRetiro < self._saldo) and (self._saldo > 0):
            self._saldo -= cantidadRetiro
            return f"Retiro Existoso!!!, Saldo Actual: {self._saldo}"
        else:
            return f"Saldo Insuficiente"

    def modificarPassword(self, nuevoPassword):
        self.__password = nuevoPassword
        return f"Password Modificado!!!, Nuevo Password: {self.__password}"

cuentaBancaria1 = CuentaBancaria("FGALVEZ", 1000000, 1937)
print(cuentaBancaria1.titular)
print(cuentaBancaria1._saldo)

print(cuentaBancaria1.depositar(1500000))

print(cuentaBancaria1.retirar(500000))

print(cuentaBancaria1.modificarPassword(1234))

