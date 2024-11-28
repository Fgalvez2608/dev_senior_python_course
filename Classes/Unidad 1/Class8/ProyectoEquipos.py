import datetime

listaDeEquipos = [
    ["equipo 1", "01/01/1924", "Futbol", [2, 2, 1, 2, 3]],
    ["equipo 2", "01/01/1934", "Basquet", [0, 2, 0, 2, 1]]
]

def agregarEquipo():
    try:
        print("\n ------ REGISTRAR EQUIPO ------")
        nombreEquipo = input("Ingrese el nombre del equipo: ")
        fechaFundacion = input("Ingrese la fecha de fundacion del equipo: ")
        tipoDeportivo = input("Ingrese el tipo de deporte del equipo: ")
        resultados = list(map(int, input("Ingrese los puntos obtenidos separados por comas: ").split(",")))
        listaDeEquipos.append([nombreEquipo, fechaFundacion, tipoDeportivo, resultados])
        print("Equipo registrado exitosamente")
        print("")
    except ValueError:
        print("Error al agregar el equipo, verifique la informacion ingresada")

# 2. Funcion para visualizar resultados de los experimentos
def visualizaEquipos():
    print("\n ------ EQUIPOS REGISTRADOS ------")
    for i, equipo in enumerate(listaDeEquipos):
        print(f"Equipo {i+1}:")
        print(f"Nombre: {equipo[0]}")
        print(f"Fecha Fundacion: {equipo[1]}")
        print(f"Tipo Deportivo: {equipo[2]}")
        print(f"Resultados: {equipo[3]}")
        print("")

# 3. Funcion para eliminar experimento
def eliminarEquipos():
    pass

# 4. Funcion para calculo estadistico basico (PROMEDIO - VALOR MAXIMO - VALOR MINIMO).
def analisisResultados():
    visualizaEquipos()
    index = int(input("Ingrese el numero del equipo que desea analizar: "))
    
    if 0 <= index < len(listaDeEquipos):
        resultados = listaDeEquipos[index][3]
        promedio = sum(resultados) / len(resultados)
        maximo = max(resultados)
        minimo = min(resultados)
        print(f"Estadisticas del equipo {listaDeEquipos[index][0]}")
        print(f"Promedio: {promedio}")
        print(f"Maximo: {maximo}")
        print(f"Minimo: {minimo}")
        

# 5. Funcion para comprar 2 o mas experimentos
def compradorEquipos():
    visualizaEquipos()
    indices = list(map(int, input("Ingrese los numeros de los equipos que desea comprar separados por comas: ").split(",")))
    resultadosComprados = []
    for index in indices:
        if 0 <= index < len(listaDeEquipos):
            promedio = sum(listaDeEquipos[index][3]) / len(listaDeEquipos[index][3])
            resultadosComprados.append(promedio)
        else:
            print(f"Indice {index} no valido")
    resultadosComprados.sort()
    print("Resultados Comparados")
    for index, promedio in resultadosComprados:
        print(f"{index + 1}. {listaDeEquipos[index][0]} - {promedio}")

# 6. Funcion para generar reporte con un archivo txt
def generarReporte():
    pass

# 7. Funcion para menu principal
def menuPrincipal():
    pass

if __name__ == "__main__": # linea de codigo que ejecuta la funcion principal
    menuPrincipal()

