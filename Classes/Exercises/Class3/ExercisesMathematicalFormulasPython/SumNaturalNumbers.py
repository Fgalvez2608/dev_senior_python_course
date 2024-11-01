"""
Ejercicio: Sum of Natural Numbers ➕
La suma de los primeros ( n ) números naturales se calcula con la fórmula:

[{\displaystyle \sum _{k=1}^{n}k={\frac {n(n+1)}{2}}}]

Instrucciones:
Pide al usuario un número entero positivo.
Usa la fórmula para calcular la suma de los primeros ( n ) números naturales.
Muestra el resultado en pantalla.
"""

# This Python code is a program that calculates the sum of the first `n` natural numbers based on the
# formula provided in the comments. Here's a breakdown of what each part of the code does:
print("Bienvenido a la suma de los primeros ( n ) números naturales ➕")
num = int(input("Ingresa un numero entero positivo: "))
sum = (num * (num + 1)) / 2
print(f"La suma de los primeros {num} números naturales es {sum}")

# Calcula la suma de los primeros ( n ) números naturales sin usar la fórmula
# This part of the code is an alternative way to calculate the sum of the first `n` natural numbers
# without using the formula provided in the comments. Here's a breakdown of what it does:
num2 = int(input("Ingresa un numero entero positivo: "))
sum2 = 0 # inicializar la suma a 0
for i in range(1, num2 + 1):
    sum2 += i
print(f"La suma de los primeros {num2} números naturales es {sum2}")


