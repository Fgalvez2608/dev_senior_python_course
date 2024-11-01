"""
Ejercicio 2: Calculadora de Notas
Crea un programa que pida al usuario su calificación (entre 0 y 100). Dependiendo del valor ingresado, el programa debe mostrar si el 
estudiante ha aprobado (60 o más) o ha reprobado (menos de 60). Usa condicionales para determinar el resultado.
"""
# This Python code is a program that acts as a grade calculator. It prompts the user to input their
# grade (between 0 and 100) and then determines whether the student has passed (60 or above) or failed
# (below 60).
print("Bienvenido a la Calculadora de Notas")
nota = int(input("Ingrese su nota: "))
if nota >= 60 and nota <= 100:
    print("Felicidades, has aprobado")
elif nota >= 0 and nota < 60:
    print("Lo siento, has reprobado")
else:
    print("Por favor ingrese una calificacion entre 0 y 100")

