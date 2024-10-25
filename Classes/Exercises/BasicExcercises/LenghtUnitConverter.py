# Ejercicio: Conversión de Unidades
#Crea un programa que convierta una medida en metros a centímetros y milímetros. El programa debe pedir al usuario que ingrese una longitud en metros y luego mostrar el resultado en las dos unidades.
print("Bienvenido al Conversor de Unidades de Longitud (Metros a Centimetros y Metros a Milimetros)")
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