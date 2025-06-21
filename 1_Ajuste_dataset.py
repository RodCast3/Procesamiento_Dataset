import os
import cv2
import numpy as np
from PIL import Image
import Prueba_de_Filtros as filtros

def procesar_dataset(input_dir, output_dir):
    """
    Procesa todas las imágenes en input_dir y guarda los resultados en output_dir,
    manteniendo la misma estructura de carpetas.
    """
    # Crear el directorio de salida si no existe
    os.makedirs(output_dir, exist_ok=True)
    x = 0
    # Recorrer todas las carpetas y subcarpetas
    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                # Rutas completas
                input_path = os.path.join(root, filename)
                relative_path = os.path.relpath(root, input_dir)
                output_subdir = os.path.join(output_dir, relative_path)
                output_path = os.path.join(output_subdir, filename)
                
                # Crear subdirectorio en output si no existe
                os.makedirs(output_subdir, exist_ok=True)
                
                try:
                    # Procesamiento de la imagen
                    with Image.open(input_path) as pil_img:
                        # Convertir PIL a OpenCV (BGR)
                        img_cv2 = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
                        
                        # Aplicar filtros
                        img_procesada = filtros.acondicionamiento(img_cv2)
                        
                        # Convertir de vuelta a PIL (RGB) y guardar
                        img_pil = Image.fromarray(cv2.cvtColor(img_procesada, cv2.COLOR_BGR2RGB))
                        img_pil.save(output_path)
                    x += 1

                except Exception as e:
                    print(f"Error al procesar {input_path}: {str(e)}")
    print(f"Total de imágenes procesadas: {x}")


if __name__ == "__main__":
    # Configuración de rutas
    dataset_original = "Dataset_Vexel"  # Ruta del dataset original
    dataset_procesado = "Dataset_Procesado"  # Ruta del nuevo dataset
    
    # Procesar todo el dataset
    procesar_dataset(dataset_original, dataset_procesado)
    
    print("¡Procesamiento completado!")