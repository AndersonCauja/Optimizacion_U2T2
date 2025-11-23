import time

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primos_en_rango(inicio, fin):
    primos = []
    for num in range(inicio, fin + 1):
        if es_primo(num):
            primos.append(num)
    return primos

inicio_tiempo = time.time()
primos = primos_en_rango(1, 100000)
tiempo_total = time.time() - inicio_tiempo

print(f"Se encontraron {len(primos)} números primos.")
print(f"Tiempo de ejecución: {tiempo_total:.4f} segundos.")