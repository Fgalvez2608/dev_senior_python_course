from prettytable import PrettyTable


inventario = {
    "1063fg2608" : {
        "nombreProducto" : "kit de arrastre",
        "modelo" : "125",
        "cantidad" : 5,
        "fechaIngreso" : "2023-01-01",
        "fechaUltimaVenta" : "2024-11-12",
        "precio" : 1000
    },
    "1063fg2609" : {
        "nombreProducto" : "cilindro",
        "modelo" : "150",
        "cantidad" : 15,
        "fechaIngreso" : "2022-11-21",
        "fechaUltimaVenta" : "2024-11-01",
        "precio" : 5000
    }
}

def crearProducto():
    pass

def mostrarInventario():
    
    if inventario:
        print("")
        print("------- Inventario -------")
        table = PrettyTable()
        table.field_names = ["Serial", "Nombre", "Modelo", "Cantidad", "Fecha de Ingreso", "Fecha de Ultima Venta", "Precio"]
        for producto in inventario:
            table.add_row([producto, inventario[producto]['nombreProducto'], 
                        inventario[producto]['modelo'], 
                        inventario[producto]['cantidad'], 
                        inventario[producto]['fechaIngreso'], 
                        inventario[producto]['fechaUltimaVenta'], 
                        inventario[producto]['precio']], divider=True)
        print(table)
    else:
        print("El inventario esta vacio")

def actualizarInventario():
    pass

def eliminarProducto():
    mostrarInventario()
    opcionEliminar = input("Ingrese el serial del producto que desea eliminar: ")
    if opcionEliminar in inventario:
        del inventario[opcionEliminar]
        print("Producto eliminado")
    else:
        print("Producto no encontrado")

def main():
    
    while True:#funcion principal donde arranca el programa
        print("Bienvenido al sistema de inventario")
        print("1. Mostrar Inventario")
        print("2. Crear producto")
        print("3. Actualizar Inventario")
        print("4. Eliminar Proyecto")
        print("5. Salir")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            mostrarInventario()
        elif opcion == "2":
            crearProducto()
        elif opcion == "3":
            actualizarInventario()
        elif opcion == "4":
            eliminarProducto()
        elif opcion == "5":
            break
        else:
            print("Opcion no valida")
            print("Por favor elija una opcion entre 1 a 5")
            print("")

main()

