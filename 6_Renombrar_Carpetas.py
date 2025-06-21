import os
import shutil

def reindexar_carpetas(dataset_path):
    """
    Renombra carpetas de personas para que tengan índices consecutivos (1, 2, 3...).
    
    Args:
        dataset_path (str): Ruta del dataset (ej: 'Dataset_Entrenamiento').
    """
    # Obtener todas las carpetas de personas y ordenarlas numéricamente
    carpetas_personas = []
    for nombre in os.listdir(dataset_path):
        if os.path.isdir(os.path.join(dataset_path, nombre)) and nombre.startswith("PERSONA"):
            try:
                num = int(nombre.split()[1])
                carpetas_personas.append((num, nombre))
            except (IndexError, ValueError):
                continue
    
    # Ordenar por número actual
    carpetas_personas.sort()
    
    # Reindexar desde 1
    contador = 1
    for num_actual, nombre_actual in carpetas_personas:
        carpeta_actual = os.path.join(dataset_path, nombre_actual)
        nuevo_nombre = f"PERSONA {contador}"
        carpeta_nueva = os.path.join(dataset_path, nuevo_nombre)
        
        # Evitar conflicto si ya existe una carpeta con el nuevo nombre
        if os.path.exists(carpeta_nueva):
            temp_nombre = f"PERSONA_temp_{contador}"
            temp_path = os.path.join(dataset_path, temp_nombre)
            shutil.move(carpeta_actual, temp_path)
            carpeta_actual = temp_path
        
        shutil.move(carpeta_actual, carpeta_nueva)
        print(f"Renombrado: {nombre_actual} -> {nuevo_nombre}")
        contador += 1

if __name__ == "__main__":
    dataset_entrenamiento = "Dataset_Entrenamiento"
    reindexar_carpetas(dataset_entrenamiento)
    print("\n¡Reindexación completada!")