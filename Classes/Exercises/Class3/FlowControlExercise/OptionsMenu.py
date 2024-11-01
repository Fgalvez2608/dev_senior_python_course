"""
Ejercicio 4: Menú de Opciones
Crea un programa que muestre un menú de opciones simples (por ejemplo, "1. Saludar", "2. Despedirse", "3. Salir") y permita al usuario 
seleccionar una opción. Dependiendo de la opción, el programa debe ejecutar una acción específica o salir del bucle si el usuario elige 
"Salir". Usa un bucle while para mostrar el menú hasta que el usuario decida salir.
"""
# This Python code snippet creates a simple menu of options for the user to interact with. Here's a
# breakdown of what the code does:
print("Bienvenido al Menu de Opciones")
salir = True
while salir:
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        print("Hola querido estudiante")
    elif opcion == "2":
        print("Adios!!!")
    elif opcion == "3":
        salir = False
    else:
        print("Opcion no valida, Vuelve a intentarlo")
        print("Por favor elija una opcion del 1 al 3")


