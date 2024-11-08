


#Crear Listas para almacenar la informacion de los alumnos, cursos, profesores y horarios
alumnos = []
cursos = ["Java", "Python"] #en la rubrica esta descrita los 2 cursos
docentes = []
horarios = []

# Diccionarios tienen un id o llave y un valor; id and value
#estudiante = {}

#----------Creacion de funciones----------

# 1.Funcion para matriculr alumnos
def matricularAlumno():
    """
    The function `matricularAlumno` allows a user to input a student's name and select a course to
    enroll them in from a list of available courses, adding the student to a list of enrolled students
    with their chosen course.
    """
    nombreAlumno = input("Ingrese el nombre del alumno: ")
    print("Seleccione el curso a matricular: ")
    for i, curso in enumerate(cursos): #el ciclo for es para mostrarle al usuario los cursos y enumerate es una funcion para enumerar lo que hay dentro de una lista
        print(f"{i+1}: {curso}")
    
    cursoSeleccionado = int(input("Ingrese el numero del curso: "))
    
    if cursoSeleccionado >= 1 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]
        estudiante = {
            "nombre": nombreAlumno,
            "curso": curso
        }
        alumnos.append(estudiante) #linea que agrega el estudiante a la lista alumnos, es una lista de diccionarios
        print(f"El Alumno {nombreAlumno} ha sido matriculado en el curso {curso}")
    else:
        print(f"Opcion invalida!!!, solo hay {len(cursos)} cursos disponibles")

# 2.Funcion para asignar un docente a un curso
def asignarDocente():
    """
    This Python function allows the user to assign a teacher to a selected course from a list of
    courses.
    """
    print("Seleccione el curso al que desea asignar un docente: ")
    for i, curso in enumerate(cursos):
        print(f"{i+1}: {curso}")
    
    cursoSeleccionado = int(input("Ingrese el numero del curso: "))
    if cursoSeleccionado >= 1 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]
        nombreDocente = input("Ingrese el nombre del docente: ")
        docente = {
            "nombre": nombreDocente,
            "curso": curso
        }
        docentes.append(docente) #linea que agrega el docente a la lista docentes, es una lista de diccionarios
        print(f"El Docente {nombreDocente} ha sido asignado al curso {curso}")
    else:
        print(f"Opcion invalida!!!, solo hay {len(cursos)} cursos disponibles")

# 3. Funcion para asignar un horario a un curso
def asignarHorario():
    """
    This Python function allows a user to assign a schedule (days and time) to a selected course from a
    list of courses.
    """
    print("Seleccione el curso al que desea asignar un horario: ")
    for i, curso in enumerate(cursos):
        print(f"{i+1}: {curso}")
    
    cursoSeleccionado = int(input("Ingrese el numero del curso: "))
    if cursoSeleccionado >= 1 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]
        dias = input("Ingrese los dias de la semana (Ej: Martes y Jueves): ")
        hora = input("Ingrese la hora de cada clase (Ej: 8 pm a 10 pm): ")
        horario = {
            "curso": curso,
            "dias": dias,
            "hora": hora
        }
        horarios.append(horario) #linea que agrega el horario a la lista horarios, es una lista de diccionarios
        print(f"El horario {dias} de {hora} ha sido asignado al curso {curso}")
    else:
        print(f"Opcion invalida!!!, solo hay {len(cursos)} cursos disponibles")

# 4. Funcion para mostrar la lista de alumnos
def mostrarAlumnos():
    """
    This Python function displays a list of enrolled students and their courses if there are any,
    otherwise it indicates that there are no enrolled students.
    """
    if alumnos:
        print("Lista de Alumnos Matriculados:")
        for Alumno in alumnos:
            print(f"Alumno: {Alumno['nombre']} - Curso: {Alumno['curso']}")
    else:
        print("No hay alumnos matriculados")

# 5. Funcion para mostrar la lista de docentes
def mostrarDocentes():
    """
    The function `mostrarDocentes` displays a list of assigned teachers and their respective courses.
    """
    if docentes:
        print("Lista de Docentes Asignados")
        for docente in docentes:
            print(f"Docente: {docente['nombre']} - Curso: {docente['curso']}")
    else:
        print("No hay docentes asignados")

# 6. Funcion para mostrar la lista de horarios
def mostrarHorarios():
    """
    The function `mostrarHorarios` displays a list of course schedules if they exist, otherwise it
    indicates that no schedules are assigned.
    """
    if horarios:
        print("Lista Horarios De Cursos")
        for horario in horarios:
            print(f"Dias: {horario['dias']} - Horario: {horario['hora']} - Curso: {horario['curso']}")
    else:
        print("No hay horarios asignados")

# Crear un Menu
while True:
    print("\n --- MENU DE GESTION DE MATRICULA ---")
    print("1. Matricular Alumno")
    print("2. Asignar Docente")
    print("3. Asignar Horario") 
    print("4. Mostrar Lista de Alumnos Matriculados")
    print("5. Mostrar Lista de Los Docentes Asignados")
    print("6. Mostrar Horarios de los Cursos")
    print("7. Salir")
    print("")
    
    opcion = int(input("Seleccione una opcion: ")) #Variable que almacena la opcion que elija el usuario
    
    if opcion == 1:
        matricularAlumno()
    elif opcion == 2:
        asignarDocente()
    elif opcion == 3:
        asignarHorario()
    elif opcion == 4:
        mostrarAlumnos()
    elif opcion == 5:
        mostrarDocentes()
    elif opcion == 6:
        mostrarHorarios()
    elif opcion == 7:
        break
    else:
        print("Opcion no valida")