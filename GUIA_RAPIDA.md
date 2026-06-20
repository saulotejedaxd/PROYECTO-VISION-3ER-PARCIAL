# Guia rapida para terminar la entrega

## 1. Crea el repositorio en GitHub

1. Entra a GitHub.
2. Crea un repositorio publico.
3. Sube todos los archivos de esta carpeta.
4. Comparte el repositorio con tu companero/a si aplica.

## 2. Prepara tu dataset

Tu dataset debe estar en formato YOLO. La estructura minima es:

```text
datasets/mi_dataset/images/train
datasets/mi_dataset/images/val
datasets/mi_dataset/labels/train
datasets/mi_dataset/labels/val
```

## 3. Edita `data.yaml`

Cambia los nombres de clases:

```yaml
names:
  0: clase_1
  1: clase_2
```

## 4. Entrena en Colab

Abre `colab_entrenamiento_yolo.ipynb` en Google Colab y ejecuta las celdas en orden.

Activa GPU antes de iniciar:

```text
Entorno de ejecucion > Cambiar tipo de entorno de ejecucion > GPU
```

Si prefieres entrenar desde consola:

```bash
pip install -r requirements.txt
python src/train.py --data data.yaml --epochs 50
```

## 5. Genera evidencias

```bash
python src/predict.py --weights runs/detect/train/weights/best.pt --source datasets/mi_dataset/images/val
```

## 6. Completa el README

Edita:

- Nombres de integrantes.
- Objeto o problema detectado.
- Clases del dataset.
- Caso de estudio.
- Instrucciones especificas si usaron Google Colab.

## 7. Entrega en Classroom

Ambos integrantes deben entregar la misma URL del repositorio.
