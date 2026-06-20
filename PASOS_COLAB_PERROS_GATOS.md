# Pasos para entrenar en Colab: perros y gatos

## 1. Subir el proyecto a Drive

Sube la carpeta completa `proyecto-yolo-entrega` a Google Drive.

Debe quedar asi:

```text
Mi unidad/proyecto-yolo-entrega
```

## 2. Abrir el notebook

Abre este archivo en Google Colab:

```text
colab_entrenamiento_yolo.ipynb
```

## 3. Activar GPU

En Colab:

```text
Entorno de ejecucion > Cambiar tipo de entorno de ejecucion > GPU
```

## 4. Ejecutar las celdas en orden

Ejecuta una por una.

Cuando te pida montar Drive, acepta los permisos.

## 5. Verificar ruta del proyecto

La ruta esperada es:

```python
PROJECT_DIR = Path('/content/drive/MyDrive/proyecto-yolo-entrega')
```

Si pusiste la carpeta en otro lugar, cambia esa ruta.

## 6. Entrenar

La celda de entrenamiento es:

```bash
!python src/train.py --data data.yaml --model yolov8n.pt --epochs 50 --imgsz 640 --batch 16
```

Si tarda mucho, puedes usar:

```bash
!python src/train.py --data data.yaml --model yolov8n.pt --epochs 20 --imgsz 640 --batch 16
```

## 7. Probar

Despues de entrenar, ejecuta:

```bash
!python src/predict.py --weights runs/detect/train/weights/best.pt --source datasets/mi_dataset/images/val --conf 0.25
```

## 8. Ver evidencias

Las imagenes con detecciones salen en:

```text
evidencias/predicciones/
```

Esas son las imagenes que debes subir como evidencia al repositorio.

## 9. Si aparece error en el ZIP de evidencias

Significa que todavia no existen las carpetas de resultados. Primero corre:

1. La celda de entrenamiento.
2. La celda de prediccion.
3. La celda para mostrar evidencias.
4. La celda para descargar evidencias.
