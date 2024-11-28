

#Crear Listas para almacenar la informacion de los alumnos, cursos, profesores y horarios
alumnos = [
    {"nombre": "juan", "curso": "java"},
    {"nombre": "pedro", "curso": "python"},
    {"nombre": "maria", "curso": "java"}
]
cursos = ["java", "python"] #en la rubrica esta descrita los 2 cursos
docentes = [
    {"nombre": "juan", "curso": "java"},
    {"nombre": "pedro", "curso": "python"},
    {"nombre": "maria", "curso": "java"}
]
horarios = [
    {"curso": "java", "dias": "martes y jueves", "hora": "8 am a 10 am"},
    {"curso": "python", "dias": "lunes y miercoles", "hora": "10 am a 12 pm"}
]

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

# funcion para buscar un estudiante en la lista alumnos
def buscarAlumno(nombreAlumno):
    """
    The function `buscarAlumno` searches for a student by name in a list of students and returns the
    student if found, otherwise it prints a message indicating that the student is not enrolled.
    
    :param nombreAlumno: The function `buscarAlumno(nombreAlumno)` is designed to search for a student
    by their name in a list of students called `alumnos`. If the student with the given name is found,
    the function will return the student's information. If the student is not found, it will print a
    :return: If the student with the name `nombreAlumno` is found in the `alumnos` list, then that
    student's information (dictionary) is returned. If the student is not found, a message is printed
    saying "El alumno con el nombre {nombreAlumno} no se encuentra matriculado".
    """
    for alumno in alumnos:
        if alumno["nombre"] == nombreAlumno:
            return alumno

# 2. Funcion para modificar un alumno
def modificarAlumno():
    """
    The function `modificarAlumno` allows the user to modify the course and name of a student in a
    system, with options to confirm or cancel the changes.
    """
    nombreAlumnoModificar = input("Digita el nombre del alumno a modificar: ").lower() # variable que almacena el alumno que el usuario desea modificar
    alumnoEncontrado = buscarAlumno(nombreAlumnoModificar) # variable que almacena el alumno encontrado

    if alumnoEncontrado:
        opcionCambioCurso = input("Desea cambiar el curso? (S/N): ").lower()
        if opcionCambioCurso == "s":
            print("Seleccione el curso al que se desea cambiar: ")
            for i, curso in enumerate(cursos): #el ciclo for es para mostrarle al usuario los cursos y enumerate es una funcion para enumerar lo que hay dentro de una lista
                print(f"{i+1}: {curso}")
            cursoSeleccionado = int(input("Ingrese el numero del curso: "))
            if cursoSeleccionado >= 1 and cursoSeleccionado <= len(cursos):
                cursoModificado = cursos[cursoSeleccionado - 1]
                alumnoModificado = input("Ingrese el nuevo nombre del alumno: ").lower()
                confirmacioModificacion = input("Estas seguro que deseas realizar los cambios? (S/N): ").lower()
                if confirmacioModificacion == "s":
                    alumnoEncontrado["nombre"] = alumnoModificado
                    alumnoEncontrado["curso"] = cursoModificado
                    print(f"El alumno {nombreAlumnoModificar} ha sido modificado con el curso {cursoModificado}")
                else:
                    print("No se realizo cambio de curso")
            else:
                print(f"Opcion invalida!!!, solo hay {len(cursos)} cursos disponibles")
        else:
            print("No se realizo cambio de curso")
            alumnoModificado = input("Ingrese el nuevo nombre del alumno: ").lower()
            confirmacioModificacion = input("Estas seguro que deseas realizar los cambios? (S/N): ").lower()
            if confirmacioModificacion == "s":
                alumnoEncontrado["nombre"] = alumnoModificado
    else:
        print(f"El alumno {nombreAlumnoModificar} no se encuentra matriculado")

# 3. Funcion para eliminar un alumno
def eliminarAlumno():
    """
    This Python function prompts the user to input the name of a student to be removed from a list of
    students, confirms the deletion, and then removes the student if confirmed.
    """
    nombreAlumnoEliminar = input("Digita el nombre del alumno a eliminar: ").lower() # variable que almacena el alumno que el usuario desea eliminar
    alumnoEncontrado = buscarAlumno(nombreAlumnoEliminar) # variable que almacena el alumno encontrado
    if alumnoEncontrado:    
        confirmacionEliminacion = input("Estas seguro que deseas eliminar el alumno? (S/N): ").lower()
        if confirmacionEliminacion == "s":
            alumnos.remove(alumnoEncontrado)
            print(f"El alumno {nombreAlumnoEliminar} ha sido eliminado")
        else:
            print("No se elimino el alumno")
    else:
        print(f"El alumno {nombreAlumnoEliminar} no se encuentra matriculado")

# 4.Funcion para asignar un docente a un curso
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

# Funcion para buscar un docente
def buscarDocente(curso, nombreDocente):
    for docente in docentes:
        if docente["curso"] == curso and docente["nombre"] == nombreDocente:
            return docente

# 5. Funcion para modificar un docente
def cambiarDocente():
    print("Seleccione el curso a matricular: ")
    for i, curso in enumerate(cursos): #el ciclo for es para mostrarle al usuario los cursos y enumerate es una funcion para enumerar lo que hay dentro de una lista
        print(f"{i+1}: {curso}")
    
    cursoSeleccionado = int(input("Ingrese el numero del curso: "))
    
    if cursoSeleccionado >= 1 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]
        nombreDocente = input("Ingrese el nombre del docente: ")
        if buscarDocente(curso, nombreDocente):
            confirmacionModificacion = input("Estas seguro que deseas realizar los cambios? (S/N): ").lower()
            if confirmacionModificacion == "s":
                docenteEncontrado = buscarDocente(curso, nombreDocente)
                docenteEncontrado["nombre"] = input("Ingrese el nuevo nombre del docente: ")
                print(f"El Docente {docenteEncontrado['nombre']} ha sido modificado con el curso {curso}")
            else:
                print("No se realizo cambio de docente")
        else:
            print(f"El docente {nombreDocente} no se encuentra asignado al curso {curso}!!")
    else:
        print(f"Opcion invalida!!!, solo hay {len(cursos)} cursos disponibles")


# 6. Funcion para asignar un horario a un curso
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

# 7. Funcion para modificar un horario
def modificarHorario():
    print("Horarios de los cursos Disponibles: ")
    for i, horario in enumerate(horarios):
        print(f"{i+1}: {horario['curso']} - {horario['dias']} - {horario['hora']}")
    
    horarioSeleccionado = int(input("Ingrese el numero del horario: "))
    if horarioSeleccionado >= 1 and horarioSeleccionado <= len(horarios):
        horario = horarios[horarioSeleccionado - 1] #obtiene el horario seleccionado
        confirmacionModificacion = input("Estas seguro que deseas realizar los cambios? (S/N): ").lower()
        if confirmacionModificacion == "s":
            horario["dias"] = input("Ingrese los dias de la semana (Ej: Martes y Jueves): ")
            horario["hora"] = input("Ingrese la hora de cada clase (Ej: 8 pm a 10 pm): ")
            print(f"El horario {horario['dias']} de {horario['hora']} ha sido modificado")
        else:
            print("No se realizo cambio de horario")
    else:
        print(f"Opcion invalida!!!, solo hay {len(horarios)} horarios disponibles") 

# 8. Funcion para mostrar la lista de alumnos
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

# 9. Funcion para mostrar la lista de docentes
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

# 10. Funcion para mostrar la lista de horarios
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

# 11. Funcion para mostrar el resumen del sistema
def mostrarResumen():
    
    if alumnos != []:
        print("------- Resumen del Sistema -------")
        print(f"Alumnos Matriculados: {len(alumnos)}")
        mostrarAlumnos()
        print("")
    else:
        print("No hay alumnos matriculados")
        
    if docentes != []:
        print(f"Docentes Asignados: {len(docentes)}")
        mostrarDocentes()
        print("")
    else:
        print("No hay docentes asignados")
    
    if horarios != []:
        print(f"Horarios Asignados: {len(horarios)}")
        mostrarHorarios()
        print("")
    else:
        print("No hay horarios asignados")
        
    print("------- Fin del Resumen -------")

print(alumnos)
# Crear un Menu
while True:
    print("\n ------ MENU DE GESTION DE MATRICULA ------")
    print("1. Matricular Alumno")
    print("2. Modificar Alumno")
    print("3. Eliminar Alumno")
    print("4. Asignar Docente")
    print("5. Cambio de Docente")
    print("6. Asignar Horario")
    print("7. Modificar Horario") 
    print("8. Mostrar Lista de Alumnos Matriculados")
    print("9. Mostrar Lista de Los Docentes Asignados")
    print("10. Mostrar Horarios de los Cursos")
    print("11. Resumen del Sistema")
    print("12. Salir")
    print("")
    
    opcion = int(input("Seleccione una opcion: ")) #Variable que almacena la opcion que elija el usuario
    
    if opcion == 1:
        matricularAlumno()
    elif opcion == 2:
        modificarAlumno()
    elif opcion == 3:
        eliminarAlumno()
    elif opcion == 4:
        asignarDocente()
    elif opcion == 5:
        cambiarDocente()
    elif opcion == 6:
        asignarHorario()
    elif opcion == 7:
        modificarHorario()
    elif opcion == 8:
        mostrarAlumnos()
    elif opcion == 9:
        mostrarDocentes()
    elif opcion == 10:
        mostrarHorarios()
    elif opcion == 11:
        mostrarResumen()
    elif opcion == 12:
        print("Gracias por utilizar los servicios de la Gestion de Matriculas")
        break
    else:
        print("Opcion no valida")