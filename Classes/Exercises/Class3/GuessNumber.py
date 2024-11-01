"""
Ejercicio: Adivina el Número
Escribe un programa que elija un número aleatorio entre 1 y 10. El programa debe permitir al usuario adivinar el número y darle pistas 
si su respuesta es mayor o menor al número secreto. El programa se detiene cuando el usuario acierta.
"""
import random

# Generar un número aleatorio entre 1 y 10
# This Python code is a simple number guessing game. Here's a breakdown of what each part does:
secretNumber = random.randint(1, 10)
guess = False

while not guess:
    riddle = int(input("Adivina el número (entre 1 y 10): "))
    if riddle == secretNumber:
        print("¡Felicidades! Has adivinado el número 🎉")
        guess = True
    elif riddle < secretNumber:
        print("El número secreto es mayor 📈")
    else:
        print("El número secreto es menor 📉")

