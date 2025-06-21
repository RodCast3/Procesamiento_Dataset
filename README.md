# Procesamiento_Dataset

Repositorio con scripts de preprocesamiento para acondicionar imágenes faciales y mejorar la calidad del dataset empleado en el proyecto de tesis “Sistema de control de acceso a áreas restringidas mediante reconocimiento facial y generación de códigos OTP”.

---

## 📄 Descripción

Incluye herramientas para:

- Detectar y recortar rostros automáticamente.
- Alinear y normalizar imágenes.
- Aplicar filtro Sobel para realce de bordes.

Este procesamiento se aplica al repositorio `Vexel_Dataset`, y sirve como preparación previa al entrenamiento del modelo (`Fine_Tuning_FaceNet`).

## 🧠 Tecnologías utilizadas
- Python
- OpenCV  
- NumPy / PIL  
