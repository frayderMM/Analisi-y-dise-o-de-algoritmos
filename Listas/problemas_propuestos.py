

from lista_enlazada import ListaEnlazada, Nodo

def fusionar_listas_ordenadas(lista1, lista2):
    nodo_dummy = Nodo(0)
    cola = nodo_dummy

    actual1 = lista1.cabeza
    actual2 = lista2.cabeza

    while actual1 and actual2:
        if actual1.dato < actual2.dato:
            cola.siguiente = actual1
            actual1 = actual1.siguiente
        else:
            cola.siguiente = actual2
            actual2 = actual2.siguiente
        cola = cola.siguiente

    if actual1:
        cola.siguiente = actual1
    if actual2:
        cola.siguiente = actual2

    lista_fusionada = ListaEnlazada()
    lista_fusionada.cabeza = nodo_dummy.siguiente
    return lista_fusionada

def eliminar_duplicados(lista):
    nodo_actual = lista.cabeza
    previo = None
    vistos = set()

    while nodo_actual:
        if nodo_actual.dato in vistos:
            previo.siguiente = nodo_actual.siguiente  # Eliminar nodo duplicado
        else:
            vistos.add(nodo_actual.dato)
            previo = nodo_actual
        nodo_actual = nodo_actual.siguiente
