


from lista_enlazada import ListaEnlazada
from problemas_propuestos import fusionar_listas_ordenadas, eliminar_duplicados

# Crear dos listas enlazadas ordenadas

#Crear lista uno
lista1 = ListaEnlazada()
lista1.agregar(1)
lista1.agregar(3)
lista1.agregar(5)


#Crear lista 2

lista2 = ListaEnlazada()
lista2.agregar(2)
lista2.agregar(4)
lista2.agregar(6)

# OPERACION DE Fusionar las listas
lista_fusionada = fusionar_listas_ordenadas(lista1, lista2)
print("Lista fusionada:")
lista_fusionada.imprimir_lista()

# Lista con duplicados
lista_con_duplicados = ListaEnlazada()
lista_con_duplicados.agregar(1)
lista_con_duplicados.agregar(3)
lista_con_duplicados.agregar(2)
lista_con_duplicados.agregar(3)
lista_con_duplicados.agregar(4)
lista_con_duplicados.agregar(1)

# Eliminar duplicados
eliminar_duplicados(lista_con_duplicados)
print("Lista sin duplicados:")
lista_con_duplicados.imprimir_lista()
