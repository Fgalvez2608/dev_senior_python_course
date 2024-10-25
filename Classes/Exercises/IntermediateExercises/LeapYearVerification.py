#5. Ejercicio: Verificación de Año Bisiesto 📅
#Escribe un programa que solicite un año al usuario y determine si es un año bisiesto. Un año es bisiesto si es divisible por 4 pero no por 100, a menos que también sea divisible por 400.

#Instrucciones:
#Solicita el año al usuario.
#Usa operadores aritméticos y lógicos para verificar las condiciones de un año bisiesto.
#Muestra un mensaje indicando si el año es o no bisiesto.

print("Bienvenido al Verificador de año bisiesto")
def isInteger(value):#funcion que convierte el parametro de entrada en entero y retorna: True y si no se puede convertir retorna: False
    try:
        int(value)
        return True
    except ValueError:
        return False
    
inputUsuario = input("Ingresa un año : ")
isInteger = isInteger(inputUsuario)
if not isInteger:
    inputUsuario = input("Ingresa el año: ")
year = int(inputUsuario)

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} es un ano bisiesto")
else:
    print(f"{year} no es un ano bisiesto")




