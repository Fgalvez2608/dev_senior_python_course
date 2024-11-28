# Ejercicio 4: Verificación de Edad
#Crea un programa que pida la edad del usuario y verifique si es mayor de edad (18 años o más). Usa operadores lógicos para determinar si la persona puede votar o no.
print("Bienvenido a la verificacion de edad")
def isFloat(value):#funcion que coonvierte el parametro de entrada en flotante y retorna: True y si no se puede convertir retorna: False
    try:
        float(value)
        return True
    except ValueError:
        return False

inputUsuario = input("Ingresa tu edad: ")
isFloat = isFloat(inputUsuario)
if not isFloat:
    inputUsuario = input("Ingresa tu edad nuevamente: ")
num = int(inputUsuario)

if num >= 18:
    print(f"Eres mayor de edad: {num} años!!!; SI puedes votar")
else:
    print(f"Eres menor de edad: {num} años!!!; No puedes votar")
print("")