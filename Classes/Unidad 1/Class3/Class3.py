"""
Estructuras de control de flujo 
Condicionales if, else, elif
if: se usa para verificar si una condiciones es verdadera
elif: significa "else if" y se usa para actuar si la primera condición no es verdadera
else: se usa para actuar en caso de que ninguna condición sea verdadera
"""
# The code snippet `age = int(input("Ingresa tu age: "))` is prompting the user to enter their age as
# an input, converting that input to an integer, and storing it in the variable `age`.
age = int(input("Ingresa tu age: "))
country = input("Ingresa tu pais: ")
userHasDNI = True

# The code snippet you provided is using conditional statements (`if`, `elif`, `else`) to determine
# whether a person is of legal age to buy alcoholic beverages based on their age and country.
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
# The code snippet you provided is using a `while` loop to simulate a scenario where a student is
# being checked for their eligibility to buy alcoholic beverages based on their age and country.
# Here's a breakdown of what the code is doing:
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
# The code snippet you provided is demonstrating the use of `break` and `continue` statements within
# `for` loops for control flow in Python. Here's a breakdown of what each part of the code does:
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
# The code snippet you provided is setting `user3HasDNI` to `True` and then entering a `while` loop
# that continues as long as `user3HasDNI` is `True`. Within the loop, it prompts the user to input
# their age and country, converts the age input to an integer, and stores it in `age2`. It then checks
# the conditions based on the age and country input to determine if the user can buy alcoholic
# beverages in different countries (USA, COL, GER).
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
# The code snippet `for student in range(10):` is setting up a loop that will iterate 10 times. Within
# each iteration, the user is prompted to input their age and country. The code then checks the
# conditions based on the age and country input to determine if the user can buy alcoholic beverages
# in different countries (USA, COL, GER). Depending on the age and country input, the code will print
# out messages indicating whether the user can buy alcoholic beverages in a specific country or not.
# If the user does not meet the age and country criteria, the variable `user2HasDNI` is set to `False`
# and a message indicating that the user cannot buy alcoholic beverages is printed.
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
# The code snippet you provided is setting `studenWithoutDNI` to 0 and then entering a `while` loop
# that will continue as long as `studenWithoutDNI` is less than or equal to 3. Within each iteration
# of the loop, the user is prompted to input their age and country. The code then checks the
# conditions based on the age and country input to determine if the user can buy alcoholic beverages
# in different countries (USA, COL, GER).
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
# The code snippet you provided is setting `studen2WithoutDNI` to 0 and then entering a `for` loop
# that will iterate 10,000 times. Within each iteration of the loop, the user is prompted to input
# their age and country. The code then checks the conditions based on the age and country input to
# determine if the user can buy alcoholic beverages in different countries (USA, COL, GER).
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
# The code snippet you provided is setting `studen3WithoutDNI` to 0 and then entering a `for` loop
# that will iterate 5 times. Within each iteration of the loop, the user is prompted to input their
# age and country. The code then checks if the age input is less than or equal to 14. If the age
# condition is met, it prints messages indicating that a DNI (Documento Nacional de Identidad) is
# assigned to the student, the student is registered in the system, and that the student is a native.
# It then continues to print additional information about the student. If the student is not a native,
# the code sets `isForeign` to `False` (although it is not used in this scenario). The `continue`
# statement is used to skip the remaining code block and move to the next iteration of the loop.
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
# The code snippet you provided is setting `studen4WithoutDNI` to 0 and then entering a `for` loop
# that will iterate 5 times. Within each iteration of the loop, the user is prompted to input their
# age and country. Here's a breakdown of what the code is doing:
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











