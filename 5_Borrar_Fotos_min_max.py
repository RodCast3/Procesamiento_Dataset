import os
import shutil

def filtrar_y_mostrar_eliminaciones(dataset_path, min_fotos=10, max_fotos=200):
    """
    Elimina carpetas fuera del rango [min_fotos, max_fotos] y muestra estadísticas.
    
    Args:
        dataset_path (str): Ruta del dataset (ej: 'Dataset_Entrenamiento').
        min_fotos (int): Mínimo de fotos requerido.
        max_fotos (int): Máximo de fotos permitido.
    """
    total_carpetas_eliminadas = 0
    total_fotos_eliminadas = 0
    carpetas_eliminadas = []  # Para guardar detalles

    # Recorrer todas las carpetas
    for persona_dir in os.listdir(dataset_path):
        persona_path = os.path.join(dataset_path, persona_dir)
        
        if not os.path.isdir(persona_path):
            continue

        # Contar imágenes en la carpeta
        fotos = [f for f in os.listdir(persona_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        num_fotos = len(fotos)

        # Verificar si está fuera del rango
        if num_fotos < min_fotos or num_fotos > max_fotos:
            shutil.rmtree(persona_path)
            total_carpetas_eliminadas += 1
            total_fotos_eliminadas += num_fotos
            carpetas_eliminadas.append((persona_dir, num_fotos))
            print(f"✗ Eliminada: {persona_dir} ({num_fotos} fotos)")

    # Mostrar resumen
    print("\n=== Resumen de Eliminaciones ===")
    print(f"Carpetas eliminadas: {total_carpetas_eliminadas}")
    print(f"Fotos eliminadas en total: {total_fotos_eliminadas}")

    # Mostrar detalles (opcional)
    if carpetas_eliminadas:
        print("\nDetalle por carpeta:")
        for carpeta, num in carpetas_eliminadas:
            print(f"- {carpeta}: {num} fotos")

if __name__ == "__main__":
    dataset_entrenamiento = "Dataset_Entrenamiento"
    filtrar_y_mostrar_eliminaciones(dataset_entrenamiento, min_fotos=21, max_fotos=100)