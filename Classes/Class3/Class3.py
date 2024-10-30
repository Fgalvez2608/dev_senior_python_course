"""
Estructuras de control de flujo 
Condicionales if, else, elif
if: se usa para verificar si una condiciones es verdadera
elif: significa "else if" y se usa para actuar si la primera condición no es verdadera
else: se usa para actuar en caso de que ninguna condición sea verdadera
"""
age = int(input("Ingresa tu age: "))
country = input("Ingresa tu pais: ")
userHasDNI = True

if age >= 21 :
    print("Eres mayor de age y puedes comprar bebidas alcoholicas en USA")
elif age >= 18:
    print("Eres maoyor de age en COL y puedes comprar bebidas alcoholicas, pero no en USA")
elif age >= 16:
    print("Eres mayor de age y puedes comprar bebidas alcoholicas en GER, pero no en USA ni COL")
else:
    print("Eres menor de age y no puedes comprar bebidas alcoholicas")
print("")
print("################################################")
if age >= 21 and country == "USA":
    print("Puedes comprar bebidas alcoholicas en USA")
elif age >= 18 and country == "COL":
    print("Puedes comprar bebidas alcoholicas en COL")
elif age >= 16 and country == "GER":
    print("Puedes comprar bebidas alcoholicas en GER")
else:
    userHasDNI = False
    print("No puedes comprar bebidas alcoholicas")
print("")
print("################################################")

"""
Bucles: for, while
permiten repetir una secuencia de instrucciones mientras una condición sea verdadera
for: se usa para recorrer una secuencia de elementos de una lista o una cadena de caracteres; se usa cuando se sabe de antemano cuantas veces qyeremos iterar o repetir una accion
while: se usa para recorrer una secuencia de elementos de una lista o una cadena de caracteres mientras una condición sea verdadera; se usa cuando no se sabe de antemano cuantas veces queremos iterar o repetir una accion y depende de una condicion que puede cambiar durante la ejecucion
"""
#ejemplo de for
for i in range(10):#la funcion range me da un rango de trabajo
    print(i) # imprime los numeros del 0 al 9
print("")
for i in range(5, 10):#la funcion range me da un rango de trabajo
    print(i) # imprime los numeros del 5 al 9
print("")
for i in range(0, 10, 2):#la funcion range me da un rango de trabajo
    print(i) # imprime los numeros del 0 al 9 de 2 en 2
print("")
print("################################################")
#ejemplo de while
user2HasDNI = True
studentNumber = 0
while user2HasDNI:
    studentNumber += 1
    if studentNumber == 10:
        user2HasDNI = False
        
    if age >= 21 and country == "USA":
        print("Puedes comprar bebidas alcoholicas en USA")
    elif age >= 18 and country == "COL":
        print("Puedes comprar bebidas alcoholicas en COL")
    elif age >= 16 and country == "GER":
        print("Puedes comprar bebidas alcoholicas en GER")
    else:
        user2HasDNI = False
        print("No puedes comprar bebidas alcoholicas")
print("")
print("################################################")
#uso de break y continue para buenas practicas de codificacion y legibilidad
for i in range(10):
    if i == 5:
        break
    print(i)
print("")
for i in range(10):
    if i == 5:
        continue
    print(i)    
print("")
print("################################################")
#Ejemplo de uso de break y continue
user3HasDNI = True
while user3HasDNI:
    age2 = int(input("Ingresa tu age: "))
    country2 = input("Ingresa tu pais: ")
    
    if age >= 21 and country == "USA":
        print("Puedes comprar bebidas alcoholicas en USA")
        print("")
    elif age >= 18 and country == "COL":
        print("Puedes comprar bebidas alcoholicas en COL")
        print("")
    elif age >= 16 and country == "GER":
        print("Puedes comprar bebidas alcoholicas en GER")
        print("")
    else:
        user2HasDNI = False
        print("No puedes comprar bebidas alcoholicas")
        print("")
print("")
print("################################################")
for student in range(10):
    age2 = int(input("Ingresa tu age: "))
    country2 = input("Ingresa tu pais: ")
    
    if age >= 21 and country == "USA":
        print("Puedes comprar bebidas alcoholicas en USA")
        print("")
    elif age >= 18 and country == "COL":
        print("Puedes comprar bebidas alcoholicas en COL")
        print("")
    elif age >= 16 and country == "GER":
        print("Puedes comprar bebidas alcoholicas en GER")
        print("")
    else:
        user2HasDNI = False
        print("No puedes comprar bebidas alcoholicas")
        print("")
print("")
print("################################################")
studenWithoutDNI = 0
while studenWithoutDNI <= 3:
    age2 = int(input("Ingresa tu age: "))
    country2 = input("Ingresa tu pais: ")
    
    if age >= 21 and country == "USA":
        print("Puedes comprar bebidas alcoholicas en USA")
        print("")
    elif age >= 18 and country == "COL":
        print("Puedes comprar bebidas alcoholicas en COL")
        print("")
    elif age >= 16 and country == "GER":
        print("Puedes comprar bebidas alcoholicas en GER")
        print("")
    else:
        studenWithoutDNI += 1
        print("No puedes comprar bebidas alcoholicas")
        print("")
print("")
print("################################################")
studen2WithoutDNI = 0
for student in range(10000):
    if studen2WithoutDNI == 3:
        break
    
    age2 = int(input("Ingresa tu age: "))
    country2 = input("Ingresa tu pais: ")
    
    if age >= 21 and country == "USA":
        print("Puedes comprar bebidas alcoholicas en USA")
        print("")
    elif age >= 18 and country == "COL":
        print("Puedes comprar bebidas alcoholicas en COL")
        print("")
    elif age >= 16 and country == "GER":
        print("Puedes comprar bebidas alcoholicas en GER")
        print("")
    else:
        studen2WithoutDNI += 1
        print("No puedes comprar bebidas alcoholicas")
        print("")
print("")
print("################################################")
studen3WithoutDNI = 0
for student in range(5):
    age2 = int(input("Ingresa tu age: "))
    country2 = input("Ingresa tu pais: ")
    
    if age <=14:
        print("A este estudiante se le asigno un DNI")
        print("Este estudiante se registro en el sistema")
        isNative = True
        if isNative:
            print("Este estudiante es nativo")
            print("Este estudiante ...")
            print("Este estudiante ...")
            print("Este estudiante ...")
            continue
        isForeign = False
        if isForeign:
            print("Este estudiante es extranjero")
            print("Este estudiante ...")
            print("Este estudiante ...")
            print("Este estudiante ...")
print("")
print("################################################")
studen4WithoutDNI = 0
for student in range(5):
    age2 = int(input("Ingresa tu age: "))
    country2 = input("Ingresa tu pais: ")
    
    if country == "USA":
        print("Tu no eres de Colombia, por favor siguiente estudiante")
        continue
    
    if age <= 15:
        print("No puedes comprar bebidas alcoholicas")
        print("Sigues en la secundaria")
        continue
    if age >= 18 and country == "COL":
        print("Se le asigno un DNI")
        print("Puedes comprar bebidas alcoholicas en COL")
        print("Estas en la universidad")
        break
print("")
print("################################################")











