"""
Ejercicio: Factorial Calculation 🎯
El factorial de un número ( n ) (representado como ( n! )) es el producto de todos los enteros positivos hasta ( n ). La fórmula es:

[ n! = n*(n-1)(n-2) \ldots* 1 ]

Instrucciones:
Crea un programa que pida un número al usuario y calcule su factorial usando un bucle.
Muestra el resultado en pantalla.
"""

# This Python code is a program that calculates the factorial of a number entered by the user. Here's
# a breakdown of what each part of the code does:
print("Bienvenido a la Calculadora de Factoriales 🎯")
num = int(input("Ingresa un numero: "))
factorial = 1 # inicializar el factorial a 1 ya que hasta ese numero es que vamos a llegar
for numero in range(1, num + 1):
    factorial *= numero
print(f"El factorial de {num} es {factorial}")


