# Ejercicio 2: Conversión de Unidades
#Crea un programa que convierta una medida en metros a centímetros y milímetros. El programa debe pedir al usuario que ingrese una longitud en metros y luego mostrar el resultado en las dos unidades.
print("Bienvenido a la Conversor de Unidades")
def isFloat(value):#funcion que coonvierte el parametro de entrada en flotante y retorna: True y si no se puede convertir retorna: False
    try:
        float(value)
        return True
    except ValueError:
        return False

inputUsuario1 = input("Ingresa una longitud en metros: ")
isFloat1 = isFloat(inputUsuario1) 
if not isFloat1:
    inputUsuario1 = input("Ingresa la longitud nuevamente: ")
num1 = float(inputUsuario1)

metrosCentimetros = 100 #variable de conversion de metros a centimetros
metrosMilimetros = 1000 #variable de conversion de metros a milimetros
conversionACentimetros = num1 * metrosCentimetros
conversionAMilimetros = num1 * metrosMilimetros
print(f"La longitd ingresada: {num1} m, es equivalente a: {conversionACentimetros} cm")
print(f"La longitd ingresada: {num1} m, es equivalente a: {conversionAMilimetros} mm")
print("")

# Ejercicio 3: Comparador de Números
#Escribe un programa que solicite dos números al usuario y determine si el primer número es mayor, menor o igual al segundo. Muestra el resultado en pantalla usando operadores relacionales.
print("Bienvenido al comparador logico de numeros")
inputUsuario2 = input("Ingresa el 1er numero: ")
isFloat2 = isFloat(inputUsuario2) 
if not isFloat2:
    inputUsuario2 = input("Ingresa el 1er numero nuevamente: ")
num2 = float(inputUsuario2)

inputUsuario3 = input("Ingresa el 2do numero: ")
isFloat3 = isFloat(inputUsuario3) 
if not isFloat3:
    inputUsuario3 = input("Ingresa el 2do numero nuevamente: ")
num3 = float(inputUsuario3)

if num2 > num3:
    print(f"El 1er numero ingresado: {num2} es > al 2do numero ingresado: {num3}")
elif num2 < num3:
    print(f"El 1er numero ingresado: {num2} es < al 2do numero ingresado: {num3}")
else:
    print(f"El 1er numero ingresado: {num2} es = al 2do numero ingresado: {num3}")
print("")

# Ejercicio 4: Verificación de Edad
#Crea un programa que pida la edad del usuario y verifique si es mayor de edad (18 años o más). Usa operadores lógicos para determinar si la persona puede votar o no.
print("Bienvenido a la verificacion de edad")
inputUsuario4 = input("Ingresa tu edad: ")
isFloat4 = isFloat(inputUsuario4)
if not isFloat4:
    inputUsuario4 = input("Ingresa tu edad nuevamente: ")
num4 = int(inputUsuario4)

if num4 >= 18:
    print(f"Eres mayor de edad: {num4} años!!!; SI puedes votar")
else:
    print(f"Eres menor de edad: {num4} años!!!; No puedes votar")
print("")
