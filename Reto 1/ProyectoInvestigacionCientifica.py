#InvestigacionCientifica

from datetime import datetime #importar la libreria datetime para trabajar con fechas

#LISTAS
experimentos = [] #LISTA de diccionarios para almacenar los datos de cada experimento registrado
resultadosExperimentos = [] #LISTA para almacenar los resultados de cada experimento

#FUNCIONES
# 1.Funcion para registrar un experimento
def registrarExperimento():
    print("\n ------ REGISTRAR EXPERIMENTO ------")
    nombreExperimento = input("Ingrese el nombre del experimento: ") #Variable almacena el nombre del experimento
    fechaRealizacionString = input("Ingrese la fecha de realizacion del experimento (YYYY-MM-DD): ") #Variable de tipo string que almacena la fecha ingresada por el usuario para su validacion.
    try:
        fechaRealizacion = datetime.strptime(fechaRealizacionString, "%Y-%m-%d").strftime("%Y-%m-%d") #Variable de tipo string que almacena la fecha con la que se va a validar la fecha y se cambia el formato al solicitado
    except ValueError: # Si la fecha ingresada no cumple con el formato solicitado se muestra un mensaje de error
        print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD.") 
        return
    categoriaExperimento = input("Ingrese la categoria del experimento: ") #Variable de tipo string que almacena la categoria del experimento
    datosExperimento = int(input("Ingrese los datos del experimento: ")) #Variable de tipo int que almacena los datos del experimento
    resultadosExperimentos.append(datosExperimento) #linea de codigo que agrega los datos del experimento a la lista resultadosExperimentos

    experimento = { #DICCIONARIO para almacenar los datos de cada experimento registrado por el usuario para su posterior visualizacion o busqueda
        "nombre": nombreExperimento,
        "fecha": fechaRealizacion,
        "categoria": categoriaExperimento,
        "resultado": resultadosExperimentos
    } 
    experimentos.append(experimento) #linea de codigo que agrega el diccionario experimento a la lista experimentos
    print("Experimento registrado exitosamente")
    print("")

# 2.Funcion para visualizar un resultado

def visualizarResultados():
    if experimentos:
        print("Lista de Experimentos:")
        for experimento in experimentos:
            print(f"Nombre Experimento: {experimento['nombre']} - Fecha Experimento: {experimento['fecha']} - Categoria: {experimento['categoria']} - Resultados: {experimento['resultado']}")
    else:
        print("No hay Experimentos Registrados!!!")


# Crear un Menu
# This block of code creates a simple menu for a scientific research program. Here's what it does/Este bloque de código crea un menú simple para un programa de investigación científica:
while True:
    print("\n ------ MENU DE INVESTIGACION CIENTIFICA ------")
    print("1. GESTION DE EXPERIMENTOS")
    print("2. ANALISIS DE DATOS")
    print("3. GENERAR INFORME")
    print("4. CERRAR EL PROGRAMA")
    print("")
    
    opcionMenuPrincipal = int(input("Seleccione una opcion: ")) #Variable que almacena la opcion que elija el usuario en el menu principal
    
    if opcionMenuPrincipal == 1:
        while True:
            print("\n ------ GESTION DE EXPERIMENTOS ------")
            print("1. REGISTRAR EXPERIMENTO")
            print("2. VISUALIZAR EXPERIMENTOS")
            print("3. RETORNO AL MENU PRINCIPAL")
            print("")
            
            opcionMenuExperimento = int(input("Seleccione una opcion: ")) #Variable que almacena la opcion que elija el usuario en el menu de gestion de experimentos
            
            if opcionMenuExperimento == 1:
                registrarExperimento()
            elif opcionMenuExperimento == 2:
                visualizarResultados()
            elif opcionMenuExperimento == 3:
                print("\nSALIENDO DEL MENU DE GESTION DE EXPERIMENTOS...")
                break
            else:
                print("OPCION NO VALIDA")
                print("POR FAVOR ELIJA UNA OPCION ENTRE 1 A 3")
                print("")

    elif opcionMenuPrincipal == 2:
        while True:
            print("\n ------ ANALIS DE DATOS ------")
            print("1. PROMEDIO ")
            print("2. VALOR MAXIMO")
            print("3. VALOR MINIMO")
            print("4. RETORNO AL MENU PRINCIPAL")
            print("")
            
            opcionMenuAnalisisDatos = int(input("Seleccione una opcion: ")) #Variable que almacena la opcion que elija el usuario en el menu de gestion de experimentos
            
            if opcionMenuAnalisisDatos == 1:
                pass
            elif opcionMenuAnalisisDatos == 2:
                pass
            elif opcionMenuAnalisisDatos == 3:
                pass
            elif opcionMenuAnalisisDatos == 4:
                print("\nSALIENDO DEL MENU DE ANALISIS DE DATOS...")
                break
            else:
                print("OPCION NO VALIDA")
                print("POR FAVOR ELIJA UNA OPCION ENTRE 1 A 4")
                print("")
                
    elif opcionMenuPrincipal == 3:
        pass
    elif opcionMenuPrincipal == 4:
        print("\nSALIENDO DEL PROGRAMA...")
        break
    else:
        print("OPCION NO VALIDA")
        print("POR FAVOR ELIJA UNA OPCION ENTRE 1 A 4")
