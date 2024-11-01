#3. Ejercicio: Comparador de Números 🔍
#Escribe un programa que pida al usuario tres números. El programa debe determinar e imprimir cuál de los tres números es el mayor y cuál es el menor usando operadores relacionales.

#Instrucciones:
#Solicita tres números al usuario.
#Usa operadores relacionales (>, <) para comparar los números y determinar cuál es el mayor y cuál el menor.
#Muestra el resultado en pantalla.

print("Bienvenido al Comparador de Numeros")
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

inputUsuario3 = input("Ingresa el 3er numero: ")
isFloat3 = isFloat(inputUsuario3)

if not isFloat3:
    inputUsuario3 = input("Ingresa el 3er numero nuevamente: ")
num3 = float(inputUsuario3)

#Comparar los números
if (num1 > num2 and num1 > num3) and (num2 > num3): #evaluar el num 1 como mayor y num 3 como menor
    print(f"El 1er numero ingresado: {num1} es el mayor y el 3er numero ingresado: {num3} es el menor")
elif (num1 > num2 and num1 > num3) and (num3 > num2): #evaluar el num 1 como mayor y num 2 como menor
    print(f"El 1er numero ingresado: {num1} es el mayor y el 3er numero ingresado: {num2} es el menor")

if (num2 > num1 and num2 > num3) and (num3 > num1): #evaluar el num 2 como mayor y num 1 como menor
    print(f"El 1er numero ingresado: {num2} es el mayor y el 3er numero ingresado: {num1} es el menor")
elif (num2 > num1 and num2 > num3) and (num1 > num3): #evaluar el num 2 como mayor y num 3 como menor
    print(f"El 1er numero ingresado: {num2} es el mayor y el 3er numero ingresado: {num3} es el menor")

if (num3 > num1 and num3 > num2) and (num2 > num1): #evaluar el num 2 como mayor y num 1 como menor
    print(f"El 1er numero ingresado: {num3} es el mayor y el 3er numero ingresado: {num1} es el menor")
elif (num3 > num1 and num3 > num2) and (num1 > num2): #evaluar el num 2 como mayor y num 3 como menor
    print(f"El 1er numero ingresado: {num3} es el mayor y el 3er numero ingresado: {num2} es el menor")

print("")

