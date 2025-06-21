import os
import shutil

def clasificar_por_identity(dataset_path):
    """
    Clasifica imágenes en subcarpetas según el número de 'identity'.
    
    Args:
        dataset_path (str): Ruta del dataset principal (ej: 'Dataset_Procesado').
    """
    for persona_dir in os.listdir(dataset_path):
        persona_path = os.path.join(dataset_path, persona_dir)
        
        # Solo procesar carpetas (no archivos sueltos)
        if not os.path.isdir(persona_path):
            continue
        
        print(f"\nProcesando carpeta: {persona_dir}")
        
        for filename in os.listdir(persona_path):
            if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue
            
            # Extraer el número de 'identity' (ej: '2' en 'identity_2')
            try:
                parts = filename.split('_identity_')
                identity_part = parts[1].split('@')[0]  # Ej: '2' o '24'
                identity_num = f"Identity_{identity_part}"
            except IndexError:
                print(f"¡Formato incorrecto {filename}")
                continue
            
            # Ruta de la subcarpeta 'Identity_X'
            identity_dir = os.path.join(persona_path, identity_num)
            os.makedirs(identity_dir, exist_ok=True)
            
            # Mover el archivo a su subcarpeta
            src = os.path.join(persona_path, filename)
            dst = os.path.join(identity_dir, filename)
            
            shutil.move(src, dst)
            print(f"Movido: {filename} -> {identity_dir}")

if __name__ == "__main__":
    # Ruta del dataset principal (ajusta según tu estructura)
    dataset_principal = "Dataset_Procesado"  # Cambia esto según tu caso
    
    # Ejecutar la clasificación
    clasificar_por_identity(dataset_principal)
    
    print("\n¡Clasificación completada!")