import os
import shutil

def reorganizar_para_entrenamiento(dataset_actual, dataset_nuevo="Dataset_Entrenamiento"):
    """
    Reorganiza el dataset actual en una estructura plana por persona única.
    
    Args:
        dataset_actual (str): Ruta del dataset actual (con carpetas Identity).
        dataset_nuevo (str): Ruta del nuevo dataset (se creará si no existe).
    """
    # Crear directorio de destino
    os.makedirs(dataset_nuevo, exist_ok=True)
    
    # Contador para nombres de carpetas (PERSONA 1, PERSONA 2, ...)
    contador_personas = 1
    
    # Recorrer todas las carpetas de personas
    for persona_dir in os.listdir(dataset_actual):
        persona_path = os.path.join(dataset_actual, persona_dir)
        
        if not os.path.isdir(persona_path):
            continue
        
        # Recorrer subcarpetas Identity
        for identity_dir in os.listdir(persona_path):
            identity_path = os.path.join(persona_path, identity_dir)
            
            if not os.path.isdir(identity_path):
                continue
            
            # Crear carpeta para la persona única (PERSONA N)
            nueva_carpeta = os.path.join(dataset_nuevo, f"PERSONA {contador_personas}")
            os.makedirs(nueva_carpeta, exist_ok=True)
            
            # Copiar todas las fotos de Identity_X a PERSONA N
            for filename in os.listdir(identity_path):
                if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                    src = os.path.join(identity_path, filename)
                    dst = os.path.join(nueva_carpeta, filename)
                    shutil.copy2(src, dst)
            
            print(f"Copiadas fotos de {persona_dir}/{identity_dir} -> PERSONA {contador_personas}")
            contador_personas += 1

if __name__ == "__main__":
    # Rutas (ajustar según tu caso)
    dataset_actual = "Dataset_Procesado"  # Donde están las carpetas Identity
    dataset_nuevo = "Dataset_Entrenamiento"  # Nuevo dataset plano
    
    # Ejecutar reorganización
    reorganizar_para_entrenamiento(dataset_actual, dataset_nuevo)
    print("\n¡Dataset reorganizado con éxito!")