# lista_enlazada.py

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        ultimo_nodo = self.cabeza
        while ultimo_nodo.siguiente:
            ultimo_nodo = ultimo_nodo.siguiente
        ultimo_nodo.siguiente = nuevo_nodo

    def imprimir_lista(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.dato, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")
