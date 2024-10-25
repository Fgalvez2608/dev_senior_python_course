print("Bienvenido a la Calculadora Basica")
#funcion que coonvierte el parametro de entrada en flotante y retorna: True y si no se puede convertir retorna: False
def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

inputUsuario1 = input("Ingresa el numero 1: ")
isFloat1 = isFloat(inputUsuario1)
# num1 = float(inputUsuario1) 
#Validacion si el dato ingresado por el usuario es numerico
if not isFloat1:
    inputUsuario1 = input("Ingresa el numero 1 nuevamente: ")
num1 = float(inputUsuario1)

inputUsuario2 = input("Ingresa el numero 2: ")
isFloat2 = isFloat(inputUsuario2)
# num2 = float(inputUsuario2)
#Validacion si el dato ingresado por el usuario es numerico
if not isFloat2:
    inputUsuario2 = input("Ingresa el numero 2 nuevamente: ")
num2 = float(inputUsuario2)
print("")

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
modulo = num1 % num2
potencia = num1 ** num2

print(f"Suma: {suma}")
print(f"Resta:  {resta}")
print(f"Multiplicacion:  {multiplicacion}")
print(f"Division:  {division}")
print(f"Modulo:  {modulo}")
print(f"Potencia:  {potencia}")

print("")

print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Modulo")
print("6. Potencia")
print("")

operacion = int(input("Ingresa el numero de la operacion que deseas realizar: "))

if operacion == 1:
    print(num1 + num2)
elif operacion == 2:
    print(num1 - num2)
elif operacion == 3:
    print(num1 * num2)
elif operacion == 4:
    print(num1 / num2)
elif operacion == 5:
    print(num1 % num2)
elif operacion == 6:
    print(num1 ** num2)
else:
    print("Operacion no valida")



