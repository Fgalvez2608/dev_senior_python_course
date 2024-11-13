#sets: es parecido a una lista pero solo se puede agregar y eliminar, no se puede modificar
#set - conjunto
lenguajes = {"Java", "Python", "C++", "C#"}
#imprime el set
print(lenguajes)
print("")
#imprimir un elemento del set
#print(lenguajes[0])#error porque los sets no son indexados
#imprime la longitud del set con la funcion len(variable)
print(len(lenguajes))
print("")
#agregar un elemento al set con la funcion add(variable)
lenguajes.add("JavaScript")
print(lenguajes)
print("")
#recorrer el set con la funcion for
for lenguaje in lenguajes:
    print(lenguaje)
    print("")
#eliminar un elemento del set con la funcion remove(variable)
lenguajes.remove("C++")
print(lenguajes)
print("")
#eliminar un elemento del set con la funcion discard(variable)
lenguajes.discard("C#")
print(lenguajes)
print("")
#limpiar el set con la funcion clear()
lenguajes.clear()
print(lenguajes)
print("")
#eliminar el set con la funcion del(variable)
del lenguajes
print(lenguajes)