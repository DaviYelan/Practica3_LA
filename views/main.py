import datetime
import sys


sys.path.append('../')
from controls.calculos import Calculos
from controls.tdaArray import TDAArray
from controls.tda.linked.linkedList import Linked_List
from controls.personaControl import PersonaControl
from controls.personaDaoControl import PersonaDaoControl
from controls.censoDao import CensoDao
from controls.tda.stack.stack import Stack
from controls.tda.queque.queque import Queque
from controls.tda.linked.merge import Merge
import random
import time

#Listas enlazadas

lista = Linked_List()


# print (lista)
# lista.__addFirst__("Tamayo")
# print (lista)
# lista.__addFirst__("Curimilma")
# print (lista)
# lista.__addLast__("Guallas")
# print (lista)



#Lista enlazada añadir en posicion intermedia

# lista.__addLast__("Brian")
# print(lista)

# lista.__addLast__("Abel")
# print(lista)

# # Agregar un nodo en una posición específica
# lista.addNode("Juan", 3)
# print(lista)

# lista.addNode("Jose", 1)
# print(lista)

# #Modificar un nodo
# lista.edit("Darwin", 2)
# print(lista)

# pc = PersonaControl()

# try:
#     pc._persona._apellidos = "Cale"
#     pc._persona._nombres = "Esteban"
#     pc._persona._telefono = "0964209135"
#     pc.save
#     pc._persona = None
#     pc._persona._apellidos = "Criollo"
#     pc._persona._nombres = "Angy"
#     pc._persona._telefono = "0964209135"
#     pc.save
#     print(pc._lista)
# except Exception as error:
#     print(error)

#Eliminar un nodo
# lista.__addFirst__(1)
# print(lista)
# lista.__addLast__(2)
# print(lista)
# lista.eliminar(1)
# print(lista)

#Convertir a toArray
# lista.__addFirst__("Darwin")
# print(lista)
# lista.__addLast__("David")
# print(lista)
# lista.__addLast__("Cale")
# print(lista)

# print(lista.toArray)

#Id automatico

# try:
#     print(pc._persona)
#     pc._persona._apellidos = "Cale"
#     pc._persona._nombres = "Esteban"
#     pc._persona._telefono = "0964209135"
#     pc.save()  
#     print(pc.obtener_id())
#     #pc.saveJson()
    
#     print(pc._persona)
#     pc._persona._apellidos = "Criollo"
#     pc._persona._nombres = "Angy"
#     pc._persona._telefono = "0964209135"
#     pc.save()  
#     print(pc.obtener_id())
#     #pc.saveJson()

#     print(pc._persona)
#     pc._persona._apellidos = "Sanchez"
#     pc._persona._nombres = "Alexander"
#     pc._persona._telefono = "0964209135"
#     pc.save()  
#     print(pc.obtener_id())
#     #pc.saveJson()

#     print(pc._persona)
#     pc._persona._apellidos = "Luna"
#     pc._persona._nombres = "Miguel"
#     pc._persona._telefono = "0964209135"
#     pc.save()  
#     print(pc.obtener_id())
#     pc.saveJson()
# except Exception as error:
#     print(error)


#main ing

#pc = PersonaControl()
pcd  = PersonaDaoControl()
#cd  = CensoDao()
try:
    #pc._persona._apellidos = "Cale"
    #pc._persona._nombres = "Esteban"
    #pc._persona._telefono = "0964209135"
    #pc.save
    #pcd._persona._apellidos = "Cale"
    #pcd._persona._nombres = "Esteban"
    #pcd._persona._telefono = "0964209135"
    #pcd.save
    #pcd._persona = None        
    #print(pcd._lista)
    #pc._persona = None
    #pc._persona._apellidos = "Criollo"
    #pc._persona._nombres = "Angy"
    #pc._persona._telefono = "0964209135"
    #pcd._persona._apellidos = "Criollo"
    #pcd._persona._nombres = "Angy"
    #pcd._persona._telefono = "0964209135"
    #pc.save
    #pcd.save

    #cd.get_censo()._fecha = "2005-05-25"
    #cd.get_censo()._censador = "Isabel Morocho"
    #cd.get_censo()._peso = 50
    #cd.get_censo()._estatura = 1.75
    #cd.save()
    
    #print(pcd._lista)
    # print (cd._list())
    # print(pcd._lista)



    lista = Linked_List()
    for i in range(25000):
        lista.add(round(random.random()*1000, 2))
    #lista.print
    lista.add(32.5)
    inicio = time.time()
    lista.sort(2)
    fin = time.time()
    print(fin - inicio)
    #lista.print

    # Medir tiempo de búsqueda binaria
    # inicio = time.time()
    # result_bin = lista.binary_search("32.5")
    # fin = time.time()
    # print(f"Tiempo de búsqueda binaria: {fin - inicio} segundos")
    
    # print("Resultados de búsqueda binaria:")
    # for item in result_bin:
    #     print(item)

    # Medir tiempo de búsqueda lineal
    # inicio = time.time()
    # result_lin = lista.linear_search("32.5")
    # fin = time.time()
    # print(f"Tiempo de búsqueda lineal: {fin - inicio} segundos")
    
    # print("Resultados de búsqueda lineal:")
    # for item in result_lin:
    #     print(item)



    # listaS = Linked_List()
    # listaS.add("Morocho Isabel", listaS._length)
    # listaS.add("cale Estefania", listaS._length)
    # listaS.add("Criollo Anghy", listaS._length)
    # listaS.add("Calva David", listaS._length)
    # listaS.add("Armijos Luis", listaS._length)
    # listaS.add("Huachaca Kerly", listaS._length)
    # listaS.add("Curimilma Erika", listaS._length)
    # listaS.add("Tamayo Santiago", listaS._length)
    # listaS.add("Guaman David", listaS._length)
    # listaS.add("Tamayo Kerly", listaS._length)
    # listaS.print
    # listaS.sort(1)
    # listaS.print

    # pcd._list().print
    # listaAux = pcd._list().sort_models("_apellidos", 2)
    # listaAux.print

    # print ("Hola causa")
    # listita = listaS.search_equals("ar")
    # listita.print
    #print (("Cale".lower().__eq__("Cale".lower())))

except Exception as error:
    print("errores")
    print(error)

#print(pcd._list)
#print(cd._list)
