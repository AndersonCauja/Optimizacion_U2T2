import cProfile
import pstats
import subprocess

def ejecutar_profiling(archivo, archivo_salida):
    """Ejecuta cProfile en un archivo Python"""
    print(f" Ejecutando cProfile en: {archivo}")
    
    comando = f"python -m cProfile -o {archivo_salida} {archivo}"
    subprocess.run(comando, shell=True, capture_output=True)
    
    print(f" Profiling completado: {archivo_salida}")
    return archivo_salida

def generar_reporte_texto(archivo_prof, archivo_txt):
    """Genera un reporte legible del profiling"""
    print(f" Generando reporte: {archivo_txt}")
    
    stats = pstats.Stats(archivo_prof)
    
    with open(archivo_txt, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write(f"REPORTE DE PROFILING: {archivo_prof}\n")
        f.write("=" * 80 + "\n\n")
        
        f.write(f"TIEMPO TOTAL: {stats.total_tt:.4f} segundos\n\n")
        
        f.write("TOP 10 FUNCIONES POR TIEMPO TOTAL:\n")
        f.write("-" * 80 + "\n")
        stats.sort_stats('tottime')
        stats.print_stats(10)
        f.write("\n")
        
        f.write("TOP 10 FUNCIONES POR LLAMADAS:\n")
        f.write("-" * 80 + "\n")
        stats.sort_stats('calls')
        stats.print_stats(10)
    
    print(f" Reporte generado: {archivo_txt}")

def main():
    """Función principal para ejecutar profiling completo"""
    print(" INICIANDO PROFILING COMPLETO")
    print("=" * 60)
    
    # Ejecutar profiling en ambos códigos
    prof_original = ejecutar_profiling('codigo_original.py', 'profiling_original.prof')
    prof_optimizado = ejecutar_profiling('codigo_optimizado.py', 'profiling_optimizado.prof')
    
    print("=" * 60)
    
    # Generar reportes en texto
    generar_reporte_texto(prof_original, 'profiling_original.txt')
    generar_reporte_texto(prof_optimizado, 'profiling_optimizado.txt')
    
    print("=" * 60)
    
    # Comparar resultados
    stats_orig = pstats.Stats(prof_original)
    stats_opt = pstats.Stats(prof_optimizado)
    
    print(" COMPARATIVA FINAL DE PROFILING:")
    print(f"  Tiempo total original: {stats_orig.total_tt:.4f} segundos")
    print(f"  Tiempo total optimizado: {stats_opt.total_tt:.4f} segundos")
    
    if stats_orig.total_tt > 0:
        mejora = ((stats_orig.total_tt - stats_opt.total_tt) / stats_orig.total_tt) * 100
        print(f" Mejora en profiling: {mejora:.2f}%")
    
    print("\n PROFILING COMPLETADO")
    print(" Archivos generados:")
    print("   - profiling_original.prof")
    print("   - profiling_optimizado.prof")
    print("   - profiling_original.txt") 
    print("   - profiling_optimizado.txt")

if __name__ == "__main__":
    main()