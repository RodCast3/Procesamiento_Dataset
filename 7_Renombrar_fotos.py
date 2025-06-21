import os

def renombrar_fotos(dataset_path):
    """
    Renombra todas las fotos en el dataset con el formato 'personaN_fotoM.ext'.
    
    Args:
        dataset_path (str): Ruta del dataset (ej: 'Dataset_Entrenamiento').
    """
    for persona_dir in os.listdir(dataset_path):
        persona_path = os.path.join(dataset_path, persona_dir)
        
        # Verificar si es una carpeta de persona (ej: 'PERSONA 1')
        if not os.path.isdir(persona_path) or not persona_dir.startswith("PERSONA"):
            continue
        
        # Extraer número de persona (ej: '1' en 'PERSONA 1')
        try:
            num_persona = persona_dir.split()[1]
        except IndexError:
            continue
        
        # Listar y ordenar fotos en la carpeta
        fotos = [f for f in os.listdir(persona_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        fotos.sort()  # Orden alfabético para consistencia
        
        # Renombrar cada foto
        for i, foto in enumerate(fotos, start=1):
            extension = os.path.splitext(foto)[1].lower()  # Conservar extensión
            nuevo_nombre = f"Persona{num_persona}_foto{i}{extension}"
            src = os.path.join(persona_path, foto)
            dst = os.path.join(persona_path, nuevo_nombre)
            
            os.rename(src, dst)
            print(f"Renombrado: {persona_dir}/{foto} -> {nuevo_nombre}")

if __name__ == "__main__":
    dataset_entrenamiento = "Dataset_Entrenamiento"
    renombrar_fotos(dataset_entrenamiento)
    print("\n¡Renombrado completado!")