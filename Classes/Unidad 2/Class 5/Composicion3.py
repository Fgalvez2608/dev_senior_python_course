# Ejemplo de composicion 3
class CalcularImpuesto:
    def ejecutar(self, monto):
        return monto * 0.19

class AplicarDescuento:
    def ejecutar(self, monto, descuento):
        return monto - (monto * descuento / 100)

class GenerarRecibo:
    def ejecutar(self, monto):
        return f"Recibo Generado por: ${monto:.2f}"

class Facturacion:
    def __init__(self):
        self.pasos = []

    def agregarPaso(self, paso):
        self.pasos.append(paso)

    def procesarFactura(self, monto, descuento = 0):
        print("Procesar factura...")
        for paso in self.pasos:
            if isinstance(paso, CalcularImpuesto):
                impuesto = paso.ejecutar(monto)
                print(f"El impuesto es: ${impuesto:.2f}")
                monto += impuesto
            elif isinstance(paso, AplicarDescuento):
                monto = paso.ejecutar(monto, descuento)
                print(f"El descuento aplicado es de: ${descuento}%")
            elif isinstance(paso, GenerarRecibo):
                print(paso.ejecutar(monto))

facturacion = Facturacion()
impuesto = CalcularImpuesto()
descuento = AplicarDescuento()
recibo = GenerarRecibo()

facturacion.agregarPaso(impuesto)
facturacion.agregarPaso(descuento)
facturacion.agregarPaso(recibo)

facturacion.procesarFactura(500, 10)































