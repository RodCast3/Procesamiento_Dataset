import cv2
import numpy as np
from mtcnn import MTCNN

detector = MTCNN()

# Escalar la imagen
def ajustarImg(imagen, x, y):
    img = cv2.resize(imagen, (x, y), interpolation=cv2.INTER_AREA)
    return img

# Convertir la imagen a tipo flotante y normalizar al rango [0, 1]
def normalizar(imagen):
    img = imagen.astype(np.float32) / 255.0 # type: ignore
    return img

# Aplicar Sobel a cada canal RGB y combinar
def filtro_sobel(imagen):
    sobelx = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)
    bordes = cv2.magnitude(sobelx, sobely)

    # Normalizar bordes a [0, 1]
    bordes = cv2.normalize(bordes, None, 0, 1, cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    bordes = np.clip(bordes * 1.5, 0, 1) # Aumentar contraste de bordes

    # Realzar contraste de la imagen original para evitar opacidad
    imagen_contraste = cv2.convertScaleAbs(imagen * 255, alpha=1.0, beta=0.2)
    imagen_contraste = normalizar(imagen_contraste)  # Normalizar a [0, 1]

    # Mezclar bordes con la imagen original
    img_final = cv2.addWeighted(imagen_contraste, 0.7, bordes, 0.3, 0) #contraste 0.70 y bordes 0.30
    img_final = (img_final * 255).astype(np.uint8)
    return img_final

def detectar_y_recortar_rostro(imagen):
    """Detecta y recorta el primer rostro usando MTCNN"""
    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    resultados = detector.detect_faces(imagen_rgb)
    if not resultados:
        raise ValueError("No se detectó ningún rostro.")
    x, y, w, h = resultados[0]['box']
    x, y = max(x, 0), max(y, 0)
    return imagen[y:y+h, x:x+w]


def acondicionamiento(imagen):
    rostro = detectar_y_recortar_rostro(imagen)
    img_ajustada = ajustarImg(rostro, 160, 160)
    img_normal = normalizar(img_ajustada)
    img_final = filtro_sobel(img_normal)
    return img_final
