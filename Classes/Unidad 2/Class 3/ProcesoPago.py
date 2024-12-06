"""Interfaces en Python, se importa la libreria abstract ya que python
no tiene interfaces pero se implementan basadas en los metodos abstractos"""

from abc import ABC, abstractmethod

class ProcesoPago(ABC):

    @abstractmethod
    def procesoPago(self, cantidadDinero: float) -> None:
        pass

    @abstractmethod
    def reembolsoPago(self, transaccion: str) -> None:
        pass

class Paypal(ProcesoPago):
    
    def procesoPago(self, cantidadDinero: float) -> None:
        print(f"Proceso de pago con Paypal de ${cantidadDinero}")

    def reembolsoPago(self, transaccion: str) -> None:
        print(f"Reembolso de pago con Paypal de la transaccion {transaccion}")

class Stripe(ProcesoPago):
    
    def procesoPago(self, cantidadDinero: float) -> None:
        print(f"Proceso de pago con Stripe de ${cantidadDinero}")

    def reembolsoPago(self, transaccion: str) -> None:
        print(f"Reembolso de pago con Stripe de la transaccion {transaccion}")

    def cancelarPago(self, transaccion: str) -> None:
        print(f"Cancelacion de pago con Stripe de la transaccion {transaccion}")

if __name__ == "__main__":
    paypal = Paypal()
    stripe = Stripe()
    paypal.procesoPago(100)
    stripe.procesoPago(100)
    paypal.reembolsoPago("1234")
    stripe.reembolsoPago("1234")



