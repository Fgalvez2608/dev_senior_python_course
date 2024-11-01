"""
Ejercicio: Calculate the Hypotenuse of a Right Triangle 📐
Usa el Teorema de Pitágoras para calcular la hipotenusa de un triángulo rectángulo. La fórmula es:

[ c = \sqrt{a^2 + b^2} ]

donde ( a ) y ( b ) son los catetos del triángulo, y ( c ) es la hipotenusa.

Instrucciones:
Solicita al usuario los valores de los catetos.
Calcula la hipotenusa usando la fórmula.
Muestra el resultado en pantalla.
Usa la funcion sqrt de la libreria math de python como en el ejemplo para importar librerias.
"""
# This Python code calculates the hypotenuse of a right triangle using the Pythagorean theorem. Here's
# a breakdown of what the code does:
import math # importar la libreria math para usar la funcion sqrt
print("Bienvenido a calcular la hipotenusa de un triangulo rectangulo 📐")
a = int(input("Ingresa el valor del cateto a: "))
b = int(input("Ingresa el valor del cateto b: "))
c = math.sqrt(a**2 + b**2) # formula para calcular la hipotenusa con el uso de la funcion sqrt de la libreria math
print(f"La hipotenusa de un triangulo rectangulo con catetos {a} y {b} es {c}")


