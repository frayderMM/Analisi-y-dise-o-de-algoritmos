import time
import random

# Quicksort Clásico
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Selecciona el pivote como el elemento central
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Randomized Quicksort
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot_index = random.randint(0, len(arr) - 1)  # Selección aleatoria del pivote
        pivot = arr[pivot_index]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return randomized_quicksort(left) + middle + randomized_quicksort(right)

# Función para medir el tiempo de ejecución
def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time

# Comparación de Rendimiento
sizes = [500, 5000, 50000]
results = []

for size in sizes:
    arr = [random.randint(0, 10000) for _ in range(size)]
    
    # Medir el tiempo de Quicksort Clásico
    time_classic = measure_time(quicksort, arr[:])
    
    # Medir el tiempo de Randomized Quicksort
    time_randomized = measure_time(randomized_quicksort, arr[:])
    
    results.append((size, time_classic, time_randomized))

# Mostrar los resultados
for size, time_classic, time_randomized in results:
    print(f"Tamaño de la lista: {size}")
    print(f"Tiempo de Quicksort Clásico: {time_classic:.6f} segundos")
    print(f"Tiempo de Randomized Quicksort: {time_randomized:.6f} segundos")
    print("-" * 40)












import matplotlib.pyplot as plt

# Extraer tamaños y tiempos
sizes = [result[0] for result in results]
times_classic = [result[1] for result in results]
times_randomized = [result[2] for result in results]

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(sizes, times_classic, label='Quicksort Clásico', marker='o')
plt.plot(sizes, times_randomized, label='Randomized Quicksort', marker='o')

# Añadir título y etiquetas
plt.title('Comparación de Tiempos: Quicksort Clásico vs Randomized Quicksort')
plt.xlabel('Tamaño de la Lista')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
