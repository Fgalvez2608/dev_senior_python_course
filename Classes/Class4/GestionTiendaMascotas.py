# This Python code is a simple program for managing a pet store's inventory and sales. Here's a
# breakdown of what the code does:
import datetime

inventario = []
ventas = []
ventasTotalesAcumuladas = 0

while True:
    print("\n --- MENU DE GESTION DE MASCOTAS DEVSENIOR ---")#\n es para que se ponga un salto de linea
    print("1. Registrar Producto")
    print("1. Vender Productos")
    print("3. Mostrar Inventario Detallado")
    print("4. Historial de Ventas")
    print("5. Mostrar ventas totales")
    print("6. Salir")
    
    opcion = int(input("Seleccione una opcion: "))

    # This block of code is handling the process of registering a new product in the pet store's
    # inventory. When the user selects option 1 from the menu, the program prompts the user to input
    # details of the new product such as name, category, price, and quantity. It then creates a list
    # containing this information and appends it to the `inventario` list, which represents the
    # inventory of products in the store. Finally, it confirms to the user that the product has been
    # successfully added to the inventory.
    if opcion == 1:
        print("------------------------------")
        print("     Agregar Productos")
        print("------------------------------")
        nombre = input("Ingrese el nombre del producto: ").lower()
        categoria = input("Ingrese la categoria del producto: ").lower()
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        fechaIngreso = datetime.now().strftime("%Y-%m-%d")
        
        producto = [nombre, categoria, precio, cantidad, fechaIngreso]
        inventario.append(producto)
        print("El producto ha sido agregado al inventario")
        print("")
    
    # This block of code is handling the process of selling products in the pet store inventory
    # management system. Here's a breakdown of what it does:
    elif opcion == 2:
        print("------------------------------")
        print("     Venta de Productos")
        print("------------------------------")
        nombreProductoVenta = input("Ingrese el nombre del producto a vender: ").lower()
        
        productoEncontrado = False
        for producto in inventario:
            if producto[0] == nombreProductoVenta:
                productoEncontrado = True
                cantidadVenta = int(input("Ingrese la cantidad del producto a vender: "))
                if producto[3] >= cantidadVenta:
                    total = producto[2] * cantidadVenta
                    producto[3] -= cantidadVenta
                    fechaVenta = datetime.now().strftime("%Y-%m-%d")
                    ventas.append([nombreProductoVenta, cantidadVenta, fechaVenta, total])
                    ventasTotalesAcumuladas += total
                    print(f"Venta realizada. Total de la venta: ${total:.2f}")
                    print("------------------------------")
                else:
                    print(f"No hay suficiente stock de {nombreProductoVenta}, solo tenemos {producto[3]} unidades")
                    print("------------------------------")
                    break

        if not productoEncontrado:
            print("Producto no existe en el inventario")

# The code block you provided is handling the display of the detailed inventory of products in the pet
# store. When the user selects option 3 from the menu, this block of code is executed. Here's a
# breakdown of what it does:
    elif opcion == 3:
        print("------------------------------")
        print("   Inventario de Productos")
        print("------------------------------")
        for producto in inventario:
            print(f"Nombre: {producto[0]}")
            print(f"Categoria: {producto[1]}")
            print(f"Precio: ${producto[2]:.2f}")
            print(f"Cantidad: {producto[3]}")
            print(f"Fecha de Ingreso: {producto[4]}")
            print("------------------------------")

# The provided code block is responsible for displaying the historical record of sales in the pet
# store. When the user selects option 4 from the menu, this block of code is executed. Here's a
# breakdown of what it does:
    elif opcion == 4:
        if ventas:
            print("------------------------------")
            print("     Historial de Ventas")
            print("------------------------------")
            for venta in ventas:
                print(f"Nombre: {venta[0]}")
                print(f"Cantidad Vendida: {venta[1]}")
                print(f"Total de la Venta: ${venta[2]:.2f}")
                print(f"Fecha de la Venta: {venta[3]}")
                print("------------------------------")
        else:
            print("No hay ventas registradas")
        
# This block of code is handling the option where the user selects to display the total sales made in
# the pet store.
    elif opcion == 5:
        if ventasTotalesAcumuladas > 0:
            print(f"Las ventas totales son: {ventasTotalesAcumuladas}")
        else:
            print("No hay ventas registradas")
    
# The code block `elif opcion == 6 or opcion == "salir":` is checking if the user has selected option
# 6 or entered the string "salir" to exit the program. If either of these conditions is met, the
# program will display the message "\nSaliendo del programa, gracias por utilizar nuestro servicios"
# which translates to "Exiting the program, thank you for using our services" and then the program
# will terminate. This provides a way for the user to gracefully exit the program when they are done
# using it.
    elif opcion == 6 or opcion == "salir":
        print("\nSaliendo del programa, gracias por utilizar nuestro servcios")
    
# The code block you provided with `else:` is handling the scenario where the user enters an option
# that is not within the valid range of 1 to 6.
    else:
        print("Opcion no valida")
        print("Por favor elija una opcion entre 1 a 6")
        print("")
