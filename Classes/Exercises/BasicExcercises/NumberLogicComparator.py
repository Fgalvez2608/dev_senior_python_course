# Ejercicio 3: Comparador de Números
#Escribe un programa que solicite dos números al usuario y determine si el primer número es mayor, menor o igual al segundo. Muestra el resultado en pantalla usando operadores relacionales.
print("Bienvenido al comparador logico de numeros")
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

if num1 > num2:
    print(f"El 1er numero ingresado: {num1} es > al 2do numero ingresado: {num2}")
elif num1 < num2:
    print(f"El 1er numero ingresado: {num1} es < al 2do numero ingresado: {num2}")
else:
    print(f"El 1er numero ingresado: {num1} es = al 2do numero ingresado: {num2}")
print("")