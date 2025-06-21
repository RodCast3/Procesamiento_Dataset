import os
import random
import shutil

def balancear_dataset(dataset_path, max_fotos=30):
    """
    Elimina fotos aleatorias en carpetas con más de `max_fotos` imágenes.
    
    Args:
        dataset_path (str): Ruta del dataset (ej: 'Dataset_Entrenamiento').
        max_fotos (int): Número máximo de fotos por carpeta después del balanceo.
    """
    total_eliminadas = 0
    
    for persona_dir in os.listdir(dataset_path):
        persona_path = os.path.join(dataset_path, persona_dir)
        
        if not os.path.isdir(persona_path):
            continue
        
        # Listar imágenes válidas
        fotos = [f for f in os.listdir(persona_path) 
                 if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        num_fotos = len(fotos)
        
        # Si hay más de max_fotos, eliminar excedentes aleatoriamente
        if num_fotos > max_fotos:
            fotos_a_eliminar = random.sample(fotos, num_fotos - max_fotos)
            for foto in fotos_a_eliminar:
                os.remove(os.path.join(persona_path, foto))
                total_eliminadas += 1
            
            print(f"{persona_dir}: Se eliminaron {len(fotos_a_eliminar)} fotos (ahora tiene {max_fotos})")
    
    print(f"\nTotal de fotos eliminadas: {total_eliminadas}")

if __name__ == "__main__":
    # Configuración
    dataset_path = "Dataset_Entrenamiento"  # Ruta de tu dataset
    max_fotos_por_carpeta = 20             # Máximo de fotos permitidas por carpeta
    
    # Ejecutar balanceo
    balancear_dataset(dataset_path, max_fotos_por_carpeta)