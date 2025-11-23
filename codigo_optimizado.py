import time
import numpy as np

def es_primo_opt(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(np.sqrt(n)) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    return True

def primos_en_rango_opt(inicio, fin):
    return [num for num in range(inicio, fin + 1) if es_primo_opt(num)]

inicio_tiempo = time.time()
primos = primos_en_rango_opt(1, 100000)
tiempo_total = time.time() - inicio_tiempo

print(f"Se encontraron {len(primos)} números primos.")
print(f"Tiempo de ejecución optimizado: {tiempo_total:.4f} segundos.")

