class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._agregar_recursivo(valor, self.raiz)

    def _agregar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = NodoArbol(valor)
            else:
                self._agregar_recursivo(valor, nodo_actual.izquierda)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = NodoArbol(valor)
            else:
                self._agregar_recursivo(valor, nodo_actual.derecha)

    def imprimir_arbol(self, nodo=None, nivel=0):
        if nodo is not None:
            self.imprimir_arbol(nodo.derecha, nivel + 1)
            print(' ' * 4 * nivel + '->', nodo.valor)
            self.imprimir_arbol(nodo.izquierda, nivel + 1)

# Función para verificar si el árbol binario es balanceado
def es_balanceado(raiz):
    def altura(nodo):
        if nodo is None:
            return 0
        altura_izquierda = altura(nodo.izquierda)
        altura_derecha = altura(nodo.derecha)
        return max(altura_izquierda, altura_derecha) + 1

    if raiz is None:
        return True

    altura_izquierda = altura(raiz.izquierda)
    altura_derecha = altura(raiz.derecha)

    if abs(altura_izquierda - altura_derecha) > 1:
        return False

    return es_balanceado(raiz.izquierda) and es_balanceado(raiz.derecha)

# Función para contar el número de nodos hoja en el árbol binario
def contar_nodos_hoja(nodo):
    if nodo is None:
        return 0
    if nodo.izquierda is None and nodo.derecha is None:
        return 1
    return contar_nodos_hoja(nodo.izquierda) + contar_nodos_hoja(nodo.derecha)

# Código de prueba
if __name__ == "__main__":
    # Crear un árbol binario
    arbol = ArbolBinario()
    arbol.agregar(10)
    arbol.agregar(5)
    arbol.agregar(15)
    arbol.agregar(2)
    arbol.agregar(7)
    arbol.agregar(12)
    arbol.agregar(17)
    arbol.agregar(3)
    arbol.agregar(1)
    arbol.agregar(4)

    # Imprimir el árbol
    print("Árbol binario:")
    arbol.imprimir_arbol(arbol.raiz)

    # Verificar si el árbol es balanceado
    if es_balanceado(arbol.raiz):
        print("El árbol está balanceado.")
    else:
        print("El árbol no está balanceado.")

    # Contar el número de nodos hoja
    nodos_hoja = contar_nodos_hoja(arbol.raiz)
    print(f"El número de nodos hoja es: {nodos_hoja}")
