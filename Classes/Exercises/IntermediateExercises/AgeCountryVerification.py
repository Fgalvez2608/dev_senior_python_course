#2. Ejercicio: Verificación de Edad y País 🌏
#Escribe un programa que solicite al usuario su edad y su país de residencia. El programa debe verificar si el usuario tiene al menos 18 años y si vive en un país específico (por ejemplo, "España") para determinar si puede votar en las elecciones nacionales.

#Instrucciones:
#Solicita la edad y el país del usuario.
#Usa operadores relacionales para verificar si la edad es mayor o igual a 18.
#Utiliza operadores lógicos (and, or) para combinar condiciones y validar la elegibilidad.
print("Bienvenido al verificador de edad y votacion por pais")
def isInteger(value):#funcion que convierte el parametro de entrada en entero y retorna: True y si no se puede convertir retorna: False
    try:
        int(value)
        return True
    except ValueError:
        return False
    
inputUsuario = input("Ingresa tu edad: ")
isInteger = isInteger(inputUsuario)
if not isInteger:
    inputUsuario = input("Ingresa tu edad nuevamente: ")
age = int(inputUsuario)

nacionalidad = input("Ingresa tu nacionalidad: ")

if age >= 18 and nacionalidad == "España":
    print("Puedes votar")
elif age >= 18 and nacionalidad == "Colombia":
    print("Puedes votar")
elif age >= 21 and nacionalidad == "USA":
    print("Puedes votar")
else:
    print("No puedes votar")

