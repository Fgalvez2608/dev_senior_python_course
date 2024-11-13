#Diccionario: Representa una coleccion de pares clave:valor

#ejemplo de diccionario
conceptosProgramacion = {
    "POO": "Programacion Orientada a Objetos",
    "IDE": "Entorno de Desarrollo Integrado",
    "DBMS": "Sistema de Gestion de Bases de Datos",
}
#imprimir el diccionario
print(conceptosProgramacion)
print("")
#imprimir el tipo del diccionario
print(type(conceptosProgramacion))
print("")
#imprimir un elemento del diccionario
print(conceptosProgramacion["POO"])
print(conceptosProgramacion.get("IDE"))
print("")
#imprimir la longitud del diccionario
print(len(conceptosProgramacion))
print("")
#imprimir las claves del diccionario
print(conceptosProgramacion.keys())
print("")
#imprimir los valores del diccionario
print(conceptosProgramacion.values())
print("")
#imprimir el par clave:valor de un diccionario
print(conceptosProgramacion.items())
print("")
#agregar un elemento al diccionario
conceptosProgramacion["SQL"] = "Lenguaje de Consulta Estructurado"
print(conceptosProgramacion)
print("")
#modificar una valor del diccionario
conceptosProgramacion["DBMS"] = "Database Management System"
print(conceptosProgramacion)
print("")
#recorrer el diccionario con el ciclo for, recorre las claves
for key in conceptosProgramacion:
    print(key)
    print("")
#recorrer el diccionario con el ciclo for, recorre los valores
for value in conceptosProgramacion.values():
    print(value)
    print("")
#recorrer el diccionario con el ciclo for, recorre los pares clave:valor
for key, value in conceptosProgramacion.items():
    print(key + ": " + value)
    print("")
#eliminar un elemento del diccionario
del conceptosProgramacion["DBMS"]
print(conceptosProgramacion)
print("")
#limpiar el diccionario
conceptosProgramacion.clear()
print(conceptosProgramacion)
print("")
#eliminar el diccionario
del conceptosProgramacion
print(conceptosProgramacion)

