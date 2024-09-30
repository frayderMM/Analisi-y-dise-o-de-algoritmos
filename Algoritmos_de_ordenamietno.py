import time
import random
import matplotlib.pyplot as plt

# Algoritmos de ordenación

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)
    for i in range(len(arr)):
        count_arr[arr[i] - min_val] += 1
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_val] - 1] = arr[i]
        count_arr[arr[i] - min_val] -= 1
    for i in range(len(arr)):
        arr[i] = output_arr[i]
    return arr

# Función para generar listas de números aleatorios
def generate_random_list(size):
    return random.sample(range(1, size*10), size)

# Tamaños de prueba
sizes = [500, 5000, 50000]

# Benchmark de los algoritmos de ordenación
def benchmark_sorting_algorithms():
    results = {}
    
    for size in sizes:
        arr = generate_random_list(size)
        print(f"\nTesting with {size} elements:")
        
        # Bubble Sort
        start_time = time.time()
        bubble_sort(arr.copy())
        elapsed_time = time.time() - start_time
        results[f"Bubble Sort {size}"] = elapsed_time
        print(f"Bubble Sort: {elapsed_time:.5f} seconds")
        
        # Merge Sort
        start_time = time.time()
        merge_sort(arr.copy())
        elapsed_time = time.time() - start_time
        results[f"Merge Sort {size}"] = elapsed_time
        print(f"Merge Sort: {elapsed_time:.5f} seconds")
        
        # Heapsort
        start_time = time.time()
        heap_sort(arr.copy())
        elapsed_time = time.time() - start_time
        results[f"Heapsort {size}"] = elapsed_time
        print(f"Heapsort: {elapsed_time:.5f} seconds")
        
        # Radix Sort
        start_time = time.time()
        radix_sort(arr.copy())
        elapsed_time = time.time() - start_time
        results[f"Radix Sort {size}"] = elapsed_time
        print(f"Radix Sort: {elapsed_time:.5f} seconds")
        
        # Counting Sort
        start_time = time.time()
        counting_sort(arr.copy())
        elapsed_time = time.time() - start_time
        results[f"Counting Sort {size}"] = elapsed_time
        print(f"Counting Sort: {elapsed_time:.5f} seconds")
        
    return results

# Función para graficar los resultados
def plot_results(results, sizes):
    # Definir colores para cada algoritmo
    colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#33FFF9']
    
    for size in sizes:
        algorithms = [f"Bubble Sort {size}", f"Merge Sort {size}", f"Heapsort {size}", f"Radix Sort {size}", f"Counting Sort {size}"]
        times = [results[alg] for alg in algorithms]
        
        # Crear la figura y ajustar el tamaño
        plt.figure(figsize=(10, 6))
        bars = plt.bar(algorithms, times, color=colors)
        
        # Añadir título y etiquetas
        plt.title(f"Tiempos de ejecución para {size} elementos", fontsize=14)
        plt.xlabel("Algoritmo", fontsize=12)
        plt.ylabel("Tiempo (segundos)", fontsize=12)
        plt.ylim(0, max(times) * 1.1)  # Asegura que el eje y empiece en 0 y añade espacio encima de la barra
        plt.xticks(rotation=45, ha="right", fontsize=10)
        
        # Añadir etiquetas encima de cada barra
        for bar, time in zip(bars, times):
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom', fontsize=10)

        plt.tight_layout()  # Ajustar el layout para evitar solapamientos
        plt.show()

# Ejecutar las pruebas y generar gráficos
results = benchmark_sorting_algorithms()
plot_results(results, sizes)
