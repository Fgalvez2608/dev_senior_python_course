# 1.listas - List
nombres = ["juan", "pedro", "maria", "freddy"]
#impresion de la lista
print (nombres)
print("")
#imprimir un elemento de la lista
print (nombres[0])
print("")
#imprimir el ultimo elemento de la lista
print (nombres[-1])
print("")
#imprimir el segundo elemento de la lista
print (nombres[1])
print("")
# impresion del tipo de la lista con la funcion type(variable)
print (type(nombres))
print("")
# impresion por range
print (nombres[0:2])#imprime desde el elemento 0 hasta el 1
print (nombres[1:])#imprime desde el elemento 1 hasta el final
print (nombres[:2])#imprime desde el inicio hasta el 1
print (nombres[:-1])#imprime desde el inicio hasta el 1
# impresion de la longitud de la lista con la funcion len(variable)
print (len(nombres))
print("")
# agregar un elemento a la lista con la funcion append(variable)
nombres.append("jose")#agrega el elemento jose al final de la lista
print (nombres)
print("")
# agregar un elemento a la lista con la funcion insert(variable,indice)
nombres.insert(1,"flor")
print (nombres)
print("")
# eliminar un elemento de la lista con la funcion remove(variable)
nombres.remove("maria")
print (nombres)
print("")
# eliminar el ultimo elemento de la lista con la funcion pop()
nombres.pop()
print (nombres)
print("")
# eliminar un elemento de la lista con la funcion pop(indice)
nombres.pop(2)
print (nombres)
print("")
# eliminar un elemento de la lista con la funcion del(variable)
del nombres[0]
print (nombres)
print("")
#recorrer la lista con la funcion for
for nombre in nombres:#recorre la lista
    print (nombre)
    print("")
# limpiar la lista con la funcion clear()
nombres.clear()
print (nombres)
print("")
# eliminar la lista con la funcion del(variable)
del nombres
print (nombres) #imprime un error porque la lista ya no existe



