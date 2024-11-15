from datetime import datetime # importar la libreria datetime para darle formato a las fechas
import statistics # importar la libreria statistics para usar la funcion media

class Tarea:
    def __init__(self, nombre, fechaLimite, categoria, horasDedicadas): #funcion de inicializacion o metodo constructor, para recibir toda la informacion que se quiera almacenar
        self.nombre = nombre
        self.fechaLimite = fechaLimite
        self.categoria = categoria
        self.horasDedicadas = horasDedicadas

# funcion para agregar tareas
def agregarTarea(listaTareas):
    """
    Agrega una tarea a la lista de tareas. Pide al usuario la informacion de la tarea
    como nombre, fecha limite, categoria y horas dedicadas. Si el usuario ingresa
    informacion incorrecta en cuanto al formato de la fecha o las horas, se muestra
    un mensaje de error y no se agrega la tarea.
    """
    nombre = input("Ingrese el nombre de la tarea: ")
    fechaLimite_str = input("Ingrese la fecha limite de la tarea (DD/MM/AAAA): ")
    try:
        fechaLimite = datetime.strptime(fechaLimite_str, "%d/%m/%Y")
    except ValueError:
        print("Formato de fecha incorrecto. Debe ser DD/MM/AAAA.")
        return
    categoria = input("Ingrese la categoria de la tarea (Personal - Estudio - Trabajo -  Otros): ")
    horasDedicadas_str = input("Ingrese las horas dedicadas a la tarea, separadas en comas (3, 4, 5): ")
    try:
        horasDedicadas = list(map(float, horasDedicadas_str.split(","))) # se convierte la cadena de horas en una lista de floats separadas por comas con la funcion split y el objetivo de la funcion map es convertir cada elemento de la lista en un float
    except ValueError:
        print("Formato de horas incorrecto!!!")
        return
    tarea = Tarea(nombre, fechaLimite, categoria, horasDedicadas) # se crea un objeto de la clase Tarea con los datos ingresados por el usuario
    listaTareas.append(tarea)
    print("Tarea agregada exitosamente")
    print("")

def visualizarTareas(listaTareas):
    print("\n ------ VISUALIZAR TAREAS ------")
    if not listaTareas:
        print("No hay tareas registradas")
        print("")
        return
    
    for i,tarea in enumerate(listaTareas, start = 1): #enumerate es una funcion para enumerar lo que hay dentro de una lista
        print(f"Tarea {i}:")
        print(f"Nombre: {tarea.nombre}")
        print(f"Fecha Limite: {tarea.fechaLimite.strftime('%d/%m/%Y')}")
        print(f"Categoria: {tarea.categoria}")
        print(f"Horas Dedicadas: {tarea.horasDedicadas}")
        print("")# para dar un espacio entre cada tarea

def analisisHoras(listaTareas):
    print("\n ------ ANALISIS DE HORAS DEDICADAS ------")
    if not listaTareas:
        print("No hay tareas registradas para analizar")
        print("")
        return

    for tarea in listaTareas:
        print(f"Tarea: {tarea.nombre}")
        promedio = statistics.mean(tarea.horasDedicadas) # se usa la funcion mean de la libreria statistics para calcular el promedio de las horas dedicadas
        maximo = max(tarea.horasDedicadas) # se usa la funcion max de la libreria statistics para calcular el maximo de las horas dedicadas
        minimo = min(tarea.horasDedicadas) # se usa la funcion min de la libreria statistics para calcular el minimo de las horas dedicadas
        print(f"Promedio de horas dedicadas para la tarea: {promedio}")# se imprime el promedio de horas dedicadas para cada tarea
        print(f"Maximo de horas dedicadas para la tarea: {maximo}")# se imprime el maximo de horas dedicadas para cada tarea
        print(f"Minimo de horas dedicadas para la tarea: {minimo}")# se imprime el minimo de horas dedicadas para cada tarea
        print("")

def generarInforme(listaTareas):
    print("\n ------ GENERAR REPORTE ------")
    if not listaTareas:
        print("No hay tareas registradas para generar el reporte")
        print("")
        return
    
    #abrir un archivo txt
    with open("Classes/Class7/informe_tareas.txt", "w") as archivo:
        for tarea in listaTareas:
            #escribir los detalles de cada tarea en el archivo
            archivo.write(f"Nombre de la Tarea: {tarea.nombre}\n") # se escribe en el archivo el nombre de la tarea
            archivo.write(f"Fecha Limite: {tarea.fechaLimite.strftime('%d/%m/%Y')}\n") # se escribe en el archivo la fecha limite de la tarea
            archivo.write(f"Categoria: {tarea.categoria}\n") # se escribe en el archivo la categoria de la tarea
            archivo.write(f"Horas Dedicadas: {tarea.horasDedicadas}\n") # se escribe en el archivo las horas dedicadas de la tarea
            archivo.write("\n") # se escribe en el archivo un espacio en blanco

    print("Informe generado exitosamente como 'informe_tareas.txt' ")

def menu():
    listaTareas = []
    
    while True:
        print("\n ------ MENU DE OPCIONES ------")
        print("1. Agregar Tarea")
        print("2. Visualizar Tareas")
        print("3. Analisis de Datos")
        print("4. Generar Informe")
        print("5. Salir")
        print("")

        opcion = input("Ingrese la opcion que desea realizar: ")

        if opcion == "1":
            agregarTarea(listaTareas)

        elif opcion == "2":
            visualizarTareas(listaTareas)

        elif opcion == "3":
            analisisHoras(listaTareas)

        elif opcion == "4":
            generarInforme(listaTareas)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida")
            print("Por favor elija una opcion entre 1 a 5")
            print("")

if __name__ == "__main__":
    menu()






























