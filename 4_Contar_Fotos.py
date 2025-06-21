import os
from collections import defaultdict
import shutil

def contar_imagenes_por_carpeta(dataset_path):
    """
    Cuenta cuántas imágenes hay en cada carpeta y agrupa por frecuencia.
    
    Args:
        dataset_path (str): Ruta del dataset procesado.
    
    Returns:
        dict: Diccionario {número_de_imágenes: número_de_carpetas}.
    """
    contador = defaultdict(int)  # {cantidad_imgs: num_carpetas}
    
    for root, dirs, files in os.walk(dataset_path):
        # Contar solo archivos de imagen en la carpeta actual (no subcarpetas)
        imagenes = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        num_imagenes = len(imagenes)
        
        if num_imagenes > 0:
            contador[num_imagenes] += 1
    
    return contador

def generar_reporte(contador):
    """Genera un reporte legible a partir del diccionario de conteo."""
    reporte = []
    for num_imagenes, num_carpetas in sorted(contador.items()):
        if num_carpetas == 1:
            reporte.append(f"Hay {num_carpetas} carpeta con {num_imagenes} fotos")
        else:
            reporte.append(f"Hay {num_carpetas} carpetas con {num_imagenes} fotos")
    return "\n".join(reporte)


if __name__ == "__main__":
    # Ruta del dataset procesado
    dataset_procesado = "Dataset_Procesado"  # Ajustar según tu caso
    
    # Contar imágenes por carpeta
    conteo = contar_imagenes_por_carpeta(dataset_procesado)
    
    # Generar y mostrar el reporte
    print("=== Reporte del Dataset ===")
    print(generar_reporte(conteo))