# Clase para manejar la pila
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

# Función para invertir las palabras de una oración usando la pila
def invertir_palabras_en_oracion(oracion):
    palabras = oracion.split()  # Dividimos la oración en palabras
    resultado = []

    for palabra in palabras:
        pila = Pila()
        
        # Apilamos cada letra de la palabra en la pila
        for letra in palabra:
            pila.apilar(letra)
        
        # Desapilamos las letras para invertir la palabra
        palabra_invertida = ''
        while not pila.esta_vacia():
            palabra_invertida += pila.desapilar()
        
        # Añadimos la palabra invertida al resultado
        resultado.append(palabra_invertida)

    # Unimos las palabras invertidas manteniendo su posición original
    return ' '.join(resultado)

# Código de prueba
if __name__ == "__main__":
    oracion = "en otoño"
    print("Oración original:", oracion)
    
    oracion_invertida = invertir_palabras_en_oracion(oracion)
    print("Oración con palabras invertidas:", oracion_invertida)
