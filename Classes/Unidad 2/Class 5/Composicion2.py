# Ejemplo de composicion 2
class Empleado:
    def __init__(self, nombre):
        self._nombre = nombre
        self.tareas = []
    
    def agregarTarea(self, tarea):
        self.tareas.append(tarea)
    
    def ejecutarTareas(self):
        print(f"Empleado {self._nombre}, esta ejecutando las tareas:")
        for tarea in self.tareas:
            print(tarea.ejecutar())

class Tarea:
    def __init__(self):
        pass
    
    def ejecutar(self):
        pass

class TrabajoProyecto(Tarea):
    def __init__(self):
        pass
    
    def ejecutar(self):
        return ("Trabajando en el proyecto")

class Capacitacion(Tarea):
    def __init__(self):
        pass
    
    def ejecutar(self):
        return ("Realizando capacitaciones")

class Evaluacion(Tarea):
    def __init__(self):
        pass
    
    def ejecutar(self):
        return ("Realizando Evaluacion de Personal")

empleado1 = Empleado("Freddy Galvez")

proyecto = TrabajoProyecto()
capacitacion = Capacitacion()
evaluacion = Evaluacion()

empleado1.agregarTarea(proyecto)
empleado1.agregarTarea(capacitacion)
empleado1.agregarTarea(evaluacion)

empleado1.ejecutarTareas()


