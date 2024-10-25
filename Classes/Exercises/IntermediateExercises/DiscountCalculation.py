#4. Ejercicio: Cálculo de Descuento 💸
#Crea un programa que calcule el precio final de un producto con descuento. Solicita al usuario el precio original del producto y el porcentaje de descuento. El programa debe calcular y mostrar el precio final utilizando operadores aritméticos.

#Instrucciones:
#Solicita el precio original y el porcentaje de descuento.
#Usa operadores aritméticos para calcular el descuento y el precio final.
#Muestra el resultado en pantalla.
print("Bienvenido al Calculador de Descuentos")
def isFloat(value):#funcion que coonvierte el parametro de entrada en flotante y retorna: True y si no se puede convertir retorna: False
    try:
        float(value)
        return True
    except ValueError:
        return False

def isInteger(value):#funcion que convierte el parametro de entrada en entero y retorna: True y si no se puede convertir retorna: False
    try:
        int(value)
        return True
    except ValueError:
        return False
    
inputUsuario1 = input("Ingresa el valor Orginal del producto: ")
isFloat = isFloat(inputUsuario1)
if not isFloat:
    inputUsuario1 = input("Ingresa el valor nuevamente: ")
precioOriginal = float(inputUsuario1)

inputUsuario2 = input("Ingresa el porcentaje de descuento: ")
isInteger = isInteger(inputUsuario2)
if not isInteger:
    inputUsuario2 = input("Ingresa tu edad nuevamente: ")
descuento = int(inputUsuario2)

precioTotal = precioOriginal - (precioOriginal * descuento / 100)

print(f"El precio final después del descuento es: {precioTotal}")


