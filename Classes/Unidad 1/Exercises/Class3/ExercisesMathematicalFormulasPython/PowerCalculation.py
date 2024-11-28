"""
Ejercicio: Power Calculation💥
Escribe un programa que solicite al usuario dos números: la base y el exponente. El programa debe calcular la potencia utilizando la fórmula:

[ a^{n} = aaa*a \ (n\ veces)]

Instrucciones:
Solicita la base y el exponente al usuario.
Calcula la potencia utilizando el operador ** en Python.
Muestra el resultado en pantalla.
Hazlo ahora sin usar el operador **
"""

# This Python code is a program that calculates the power of a number based on user input. Here's a
# breakdown of what each part of the code does:
print("Bienvenido a la Calculadora de Potencias 💥")
print("============================================")
print("")
print("Forma 1: Con el operador **")
base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))
potencia = base ** exponente
print(f"La potencia de {base} elevado a {exponente} es {potencia}")
print("")

# Calcula la potencia sin usar el operador ** forma 1 con cilclo for
# This part of the code is calculating the power of a number without using the exponentiation operator
# `**`. Here's a breakdown of what it does:
print("Forma 2: Sin el operador **")
base2 = int(input("Ingresa la base: "))
exponente2 = int(input("Ingresa el exponente: "))
potencia2 = base
for i in range(exponente2 - 1):
    potencia2 *= base2
print(f"La potencia de {base2} elevado a {exponente2} es {potencia2}")
print("")

# Calcula la potencia sin usar el operador ** forma 1 con fun funcion pow
# This part of the code is calculating the power of a number without using the exponentiation operator
# `**` in Python. Here's a breakdown of what it does:
print("Forma 3: Con pow")
base3 = int(input("Ingresa la base: "))
exponente3 = int(input("Ingresa el exponente: "))
potencia3 = pow(base3, exponente3)
print(f"La potencia de {base3} elevado a {exponente3} es {potencia3}")
print("")

# Calcula la potencia sin usar el operador ** forma 1 con cilclo while
# This part of the code is calculating the power of a number without using the exponentiation operator
# `**` in Python. It takes user input for the base and exponent, initializes the `potencia4` variable
# to 1, and then uses a while loop to calculate the power iteratively.
print("Forma 4: Con while loop")
base4 = int(input("Ingresa la base: "))
exponente4 = int(input("Ingresa el exponente: "))
potencia4 = 1
while exponente4 > 0:
    potencia4 *= base4
    exponente4 -= 1
print(f"La potencia de {base4} elevado a {exponente4} es {potencia4}")

