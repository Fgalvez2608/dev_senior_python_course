#1. Ejercicio: Calculadora Avanzada 📐
#Crea una calculadora que tome dos números y un operador del usuario (+, -, *, /, %, **). El programa debe realizar la operación correspondiente y mostrar el resultado. Si el operador ingresado no es válido, el programa debe mostrar un mensaje de error.

#Instrucciones:
#Solicita al usuario que ingrese dos números.
#Solicita al usuario que ingrese un operador.
#Usa operadores aritméticos para realizar la operación correspondiente.
#Utiliza operadores lógicos para validar el operador ingresado.
print("Bienvenido a la calculadora avanzada")
def isFloat(value):#funcion que coonvierte el parametro de entrada en flotante y retorna: True y si no se puede convertir retorna: False
    try:
        float(value)
        return True
    except ValueError:
        return False

inputUsuario1 = input("Ingresa el 1er numero: ")
isFloat1 = isFloat(inputUsuario1)

if not isFloat1:
    inputUsuario1 = input("Ingresa el 1er numero nuevamente: ")
num1 = float(inputUsuario1)

inputUsuario2 = input("Ingresa el 2do numero: ")
isFloat2 = isFloat(inputUsuario2)

if not isFloat2:
    inputUsuario2 = input("Ingresa el 2do numero nuevamente: ")
num2 = float(inputUsuario2)

operador = input("Ingresa el operador de tu eleccion (+, -, *, /, %, **): ")

if operador == "+":
    resultado = num1 + num2
    print(f"El resultado de la suma entre {num1} + {num2} = {resultado}")
elif operador == "-":
    resultado = num1 - num2
    print(f"El resultado de la resta entre {num1} - {num2} = {resultado}")
elif operador == "*":
    resultado = num1 * num2
    print(f"El resultado de la multiplicacion entre {num1} * {num2} = {resultado}")
elif operador == "/":
    resultado = num1 / num2
    print(f"El resultado de la division entre {num1} / {num2} = {resultado}")
elif operador == "%":
    resultado = num1 % num2
    print(f"El resultado del modulo entre {num1} % {num2} = {resultado}")
elif operador == "**":
    resultado = num1 ** num2
    print(f"El resultado de la potencia entre {num1} ** {num2} = {resultado}")
else:
    print("Operador invalido")