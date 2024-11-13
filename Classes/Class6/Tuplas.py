# tuplas - Tuple
paises = ("mexico", "colombia", "brasil")
#impresion de la tupla
print (paises)
print("")
#imprimir un elemento de la tupla
print (paises[0])
print("")
#imprimir el ultimo elemento de la tupla
print (paises[-1])
print("")
#imprimir el segundo elemento de la tupla
print (paises[1])
print("")
# impresion del tipo de la tupla con la funcion type(variable)
print (type(paises))
print("")
# impresion por range
print (paises[0:2])#imprime desde el elemento 0 hasta el 1
print (paises[1:])#imprime desde el elemento 1 hasta el final
print (paises[:2])#imprime desde el inicio hasta el 1
print (paises[:-1])#imprime desde el inicio hasta el 1
# impresion de la longitud de la tupla con la funcion len(variable)
print (len(paises))
print("")
# agregar un elemento a la tupla con la funcion append(variable)
#paises.append("argentina")#imprime un error porque la tupla no puede ser modificada
paisesList = list(paises) #convierte la tupla en una lista
paisesList.append("argentina")#agrega el elemento argentina al final de la lista
paises = tuple(paisesList) #convierte la lista en una tupla
print (paises)
print("")
#cualquier modificacion de una tupla no puede ser modificado por ende, cuando se necesite agregar, eliminar o modificar la tupla se debe convertir en una lista modificarla y luego convertirla en una tupla
# agregar un elemento a la tupla con la funcion insert(variable,indice)
#paises.insert(1,"peru")#imprime un error porque la tupla no puede ser modificada
# eliminar un elemento de la tupla con la funcion remove(variable)
#paises.remove("colombia")#imprime un error porque la tupla no puede ser modificada
# eliminar el ultimo elemento de la tupla con la funcion pop()
#paises.pop()#imprime un error porque la tupla no puede ser modificada
# eliminar un elemento de la tupla con la funcion pop(indice)
#paises.pop(2)#imprime un error porque la tupla no puede ser modificada
# eliminar un elemento de la tupla con la funcion del(variable)
#del paises[0]#imprime un error porque la tupla no puede ser modificada
# limpiar la tupla con la funcion clear()
#paises.clear()#imprime un error porque la tupla no puede ser modificada
# recorrer la tupla con la funcion for
for pais in paises:#recorre la tupla
    print (pais)
    print("")
# eliminar la tupla con la funcion del(variable)
del paises
print (paises)#imprime un error porque la tupla ya no existe

