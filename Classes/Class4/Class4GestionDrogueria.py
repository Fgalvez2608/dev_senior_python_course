# This Python code is a simple program for managing a drugstore. It allows users to perform various
# actions such as registering products, selling products, displaying inventory, showing total sales,
# and exiting the program. Here's a breakdown of what each part of the code does:
print("BIENVENIDO A LA GESTION DE LA DROGUERIA")
ventasTotales = 0.0 # Inicializa la variable ventasTotales en 0 porque no hay ventas todavia

#se crean Listas para almacenar la informacion de los productos (nombres, precios, cantidades)
nombres = []
precios = []
cantidades = []

#Ciclo que haga un Menu (while) para que el usuario pueda realizar diferentes acciones
while True:
    print("\n --- MENU DE GESTION DROGUERIA---")#\n es para que se ponga un salto de linea
    print("1. Registrar producto")
    print("2. Vender productos")
    print("3. Mostrar Inventario")
    print("4. Mostrar ventas totales")
    print("5. Salir")
    print("")
    opcion = int(input("Ingrese una opcion: "))#Variable que almacena la opcion que el usuario elija
    print("")
    if opcion == 1:
        #solicitud de la cantidad de prodcutos a registrar
        cantidadProductos = int(input("Ingrese la cantidad de productos a registrar: "))

        #validacion de la cantidad de productos a registrar solo numeros positivos
        while cantidadProductos <= 0:
            print("La cantidad de productos debe ser mayor a 0")
            cantidadProductos = int(input("Ingrese la cantidad de productos a registrar: "))
            print("")
                
        print("\nRegistrar nuevo producto")
        #Ciclo para registrar o almacenar la informacion de los productos en las 3 listas
        for i in range(cantidadProductos):
            print(f"Informacion del producto {i+1}: ")

            """
            nombres[i] = input("Ingrese el nombre del producto: ")
            precios[i] = float(input("Ingrese el precio del producto: "))
            cantidades[i] = int(input("Ingrese la cantidad del producto: "))
            print("")
            """

            nombre = input("Ingrese el nombre del producto: ").lower()#.lower() es para que el nombre que ingrese el usuario se convierta en minuscula sin importar el usuario como lo escriba
            nombres.append(nombre)
            precio = float(input("Ingrese el precio del producto: "))
            precios.append(precio)
            cantidad = int(input("Ingrese la cantidad del producto: "))
            cantidades.append(cantidad)
            print("")

    elif opcion == 2:
        print("\nVender productos")
        nombreProductoVenta = input("Ingrese el nombre del producto a vender: ").lower() #variable que almacena el nombre del producto que el usuario elija para vender
        cantidadProductoVenta = int(input("Ingrese la cantidad a vender: "))#variable que almacena la cantidad de producto que el usuario elija para vender
        productoEncontrado = False #variable que almacena si el nombre del producto que el usuario elija existe o no
        for i in range(len(nombres)): #ciclo for para recorrer la lista de nombres
            if nombres[i] == nombreProductoVenta: #si el nombre del producto que el usuario elija existe en la lista de nombres
                productoEncontrado = True #la variable proyectoEncontrado se convierte en True
                if cantidadProductoVenta <= cantidades[i]: #si la cantidad de producto que el usuario elija es mayor o igual a la cantidad disponible
                    totalVenta = precios[i] * cantidadProductoVenta #se calcula el total de la venta
                    ventasTotales += totalVenta #se suma el total de la venta a la variable ventasTotales
                    cantidades[i] -= cantidadProductoVenta #se resta la cantidad de productos vendidos al inventario
                    print(f"Venta realizada. Total de la venta: ${totalVenta:.2f}")#.2f es para que se muestre el numero con 2 decimales
                    print(f"Quedan {cantidades[i]} unidades de {nombres[i]} en el inventario")
                    print("")
                else: #si la cantidad de producto que el usuario elija es menor a la cantidad disponible
                    print(f"No hay suficiente stock de {nombres[i]}, solo tenemos {cantidades[i]} unidades") 
                    print("")
                    break

        if not productoEncontrado: #si el nombre del producto que el usuario elija no existe en la lista de nombres
            print("Producto no existe en el inventario")

    elif opcion == 3:
        print("\nMostrar Inventario")
        for i in range(len(nombres)):
            print(f"Producto {i+1}: {nombres[i].capitalize()} - ${precios[i]:.2f} - Cantidad: {cantidades[i]}") #.capitalize() es para que la primer letra de cada palabra sea mayuscula
        print("")

    elif opcion == 4:
        print(f"\nVentas totales Acumuladas: ${ventasTotales:.2f}")

    elif opcion == 5:
        print("\nSaliendo del programa")
        print("Gracias por utilizar los servicios de la drogueria")
        break

    else:
        print("Opcion no valida")
        print("Por favor elija una opcion entre 1 a 4")
        print("")




