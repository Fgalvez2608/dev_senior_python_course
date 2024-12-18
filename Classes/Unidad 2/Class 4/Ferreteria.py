import threading # importa la libreria threading para trabajar con hilos
from abc import ABC, abstractmethod # importa los metodos abstractos para definir una clase abstracta

# Patron de diseno Singleton
class SistemaFacturacion:
    
    _instancia = None # atributo de clase para almacenar la instancia unica de la clase SistemaFacturacion
    _lock = threading.Lock() # atributo de clase para sincronizar hilos y evitar problemas de concurrencia

    def __new__(cls, *args, **kwargs):
        
        if not cls._instancia:
            cls._instancia = super(SistemaFacturacion, cls).__new__(cls)
            cls._instancia.inicializacionHistorico()
        return cls._instancia


        # Opcional
        """
        with cls._lock:
            if cls._instancia is None:
                cls._instancia = super(SistemaFacturacion, cls).__new__(cls)
                cls._instancia.inicializacionHistorico()
            return cls._instancia
        """
        
    def inicializacionHistorico(self):
        self.historial = []
        print("Sistema de facturacion inicializado")
    
    def registrarOperacion(self, operacion):
        self.historial.append(operacion)
        print(f"Operacion registrada: {operacion}")

# Clase abstracta
class ProcesoNegocio(ABC): #super clase o clase padre

    @abstractmethod
    def ejecutar(self):
        pass# metodo abstracto que debe ser implementado por las clases hijas

class ProcesarPedido(ProcesoNegocio): #clase hija o subclase
    def ejecutar(self):
        print("Procesando el pedido...")
        return "Pedido procesado"

class ProcesarFactura(ProcesoNegocio): #clase hija o subclase
    def ejecutar(self):
        print("Procesando la factura...")
        return "Factura procesada"

# crear la fabrica que es el patron de diseno Factory
class FabricaProcesosNegocio:
    @staticmethod
    def crearProceso(tipoProceso):
        if tipoProceso == "pedido":
            return ProcesarPedido()
        elif tipoProceso == "factura":
            return ProcesarFactura()
        else:
            raise ValueError(f"El proceso: {tipoProceso}; No existe")

if __name__ == "__main__": # bloque principal
    sistema_facturacion = SistemaFacturacion() # se instancia la clasefabrica = FabricaProcesosNegocio()
    proceso1 = FabricaProcesosNegocio.crearProceso("pedido")
    proceso2 = FabricaProcesosNegocio.crearProceso("factura")
    
    resultadoPedido1 = proceso1.ejecutar()
    sistema_facturacion.registrarOperacion(resultadoPedido1)
    
    resultadoPedido2 = proceso2.ejecutar()
    sistema_facturacion.registrarOperacion(resultadoPedido2)

    print("\nHistorico de Procesos de negocios")
    for operacion in sistema_facturacion.historial:
        print(f"Transaccion: {operacion}")





