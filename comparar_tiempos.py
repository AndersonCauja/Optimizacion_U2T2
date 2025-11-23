import time
import matplotlib.pyplot as plt
import subprocess
import sys
import numpy as np

def ejecutar_y_medir_tiempo(archivo):
    """Ejecuta un archivo Python y mide su tiempo de ejecución"""
    inicio = time.time()
    
    # Ejecutar el archivo Python
    resultado = subprocess.run([sys.executable, archivo], 
                             capture_output=True, text=True)
    
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    
    # Imprimir salida del código ejecutado
    print(f"=== SALIDA DE {archivo} ===")
    print(resultado.stdout)
    if resultado.stderr:
        print(f"Errores: {resultado.stderr}")
    
    return tiempo_ejecucion

def crear_graficos_comparativos(tiempo_original, tiempo_optimizado):
    """Crea múltiples gráficos de comparación"""
    
    # Gráfico 1: Comparación simple de barras
    plt.figure(figsize=(10, 6))
    etiquetas = ['Código Original', 'Código Optimizado']
    tiempos = [tiempo_original, tiempo_optimizado]
    colores = ['#FF6B6B', '#4ECDC4']
    
    bars = plt.bar(etiquetas, tiempos, color=colores, alpha=0.8, edgecolor='black')
    
    # Añadir valores en las barras
    for bar, tiempo in zip(bars, tiempos):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(tiempos)*0.01,
                f'{tiempo:.2f}s', ha='center', va='bottom', fontweight='bold', fontsize=12)
    
    plt.title('Comparación de Tiempos de Ejecución\nCálculo de Números Primos (1-100,000)', 
              fontsize=14, fontweight='bold')
    plt.ylabel('Tiempo (segundos)', fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    
    # Mejorar apariencia
    plt.xticks(fontweight='bold')
    plt.tight_layout()
    plt.savefig('comparacion_tiempos.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Gráfico 2: Gráfico de torta de mejora
    if tiempo_original > 0:
        mejora_porcentaje = ((tiempo_original - tiempo_optimizado) / tiempo_original) * 100
        tiempo_restante = 100 - mejora_porcentaje
        
        plt.figure(figsize=(8, 6))
        sizes = [mejora_porcentaje, tiempo_restante]
        labels = [f'Mejora\n{mejora_porcentaje:.1f}%', f'Tiempo Optimizado\n{tiempo_restante:.1f}%']
        colors = ['#00C851', '#FF4444']
        explode = (0.1, 0)  # Resaltar la mejora
        
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=90)
        plt.title('Porcentaje de Mejora del Rendimiento', fontweight='bold')
        plt.savefig('mejora_porcentaje.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    # Gráfico 3: Comparación visual (opcional para reportes)
    plt.figure(figsize=(8, 2))
    plt.barh(['Optimizado'], [tiempo_optimizado], color='#00C851', alpha=0.7, label='Optimizado')
    plt.barh(['Original'], [tiempo_original], color='#FF4444', alpha=0.7, label='Original')
    plt.xlabel('Tiempo (segundos)')
    plt.title('Comparación Visual de Tiempos')
    plt.legend()
    plt.tight_layout()
    plt.savefig('comparacion_visual.png', dpi=300, bbox_inches='tight')
    plt.show()

def main():
    print(" EJECUTANDO COMPARACIÓN DE TIEMPOS...")
    print("=" * 50)
    
    # Medir tiempo del código original
    print(" Ejecutando código original...")
    tiempo_original = ejecutar_y_medir_tiempo('codigo_original.py')
    
    print("=" * 50)
    
    # Medir tiempo del código optimizado
    print(" Ejecutando código optimizado...")
    tiempo_optimizado = ejecutar_y_medir_tiempo('codigo_optimizado.py')
    
    print("=" * 50)
    print(" RESULTADOS FINALES:")
    print(f"  Tiempo original: {tiempo_original:.4f} segundos")
    print(f" Tiempo optimizado: {tiempo_optimizado:.4f} segundos")
    
    # Calcular y mostrar mejora
    if tiempo_original > 0:
        mejora = ((tiempo_original - tiempo_optimizado) / tiempo_original) * 100
        print(f" Mejora en el rendimiento: {mejora:.2f}%")
        
        if mejora > 0:
            print(f" El código optimizado es {mejora:.2f}% más rápido")
            print(f" Se redujo el tiempo de {tiempo_original:.2f}s a {tiempo_optimizado:.2f}s")
        else:
            print(" No hubo mejora en el rendimiento")
    
    # Crear gráficos
    print("\n Generando gráficos de comparación...")
    crear_graficos_comparativos(tiempo_original, tiempo_optimizado)
    
    print(" Gráficos guardados en la carpeta actual:")
    print("   - comparacion_tiempos.png")
    print("   - mejora_porcentaje.png") 
    print("   - comparacion_visual.png")
    
    # Mostrar resumen ejecutivo
    print("\n" + "=" * 50)
    print(" RESUMEN EJECUTIVO PARA EL INFORME:")
    print(f"   Tiempo original: {tiempo_original:.4f} segundos")
    print(f"   Tiempo optimizado: {tiempo_optimizado:.4f} segundos")
    if tiempo_original > 0:
        print(f"   Mejora de rendimiento: {mejora:.2f}%")

if __name__ == "__main__":
    main()