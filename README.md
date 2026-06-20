# Deteccion de perros y gatos con YOLOv8

## Integrantes

- Elsy Cuevas - 23310379
- Saulo Tejeda - 23310404

## Descripcion del proyecto

Este proyecto aplica conceptos de Vision Artificial mediante el entrenamiento de un modelo YOLOv8 para detectar y diferenciar perros y gatos en imagenes. El objetivo principal es reconocer automaticamente animales en fotografias mediante bounding boxes, mostrando si el objeto detectado corresponde a un perro o a un gato.

El proyecto incluye codigo de entrenamiento, validacion del dataset, generacion de predicciones y evidencias visuales.

## Dataset

El dataset utilizado esta organizado en formato YOLOv8 con la siguiente estructura:

```text
datasets/mi_dataset/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

Las clases utilizadas son:

```yaml
0: perro
1: gato
```

## Requisitos

Para ejecutar el proyecto se necesitan las siguientes dependencias:

```bash
pip install -r requirements.txt
```

Tambien puede instalarse manualmente con:

```bash
pip install ultralytics opencv-python PyYAML tqdm
```

## Ejecucion del proyecto

### 1. Validar el dataset

```bash
python src/validate_dataset.py --dataset datasets/mi_dataset
```

### 2. Entrenar el modelo YOLOv8

El entrenamiento usado en el notebook es ligero para poder ejecutarse en Jupyter/GitHub Codespaces:

```bash
python src/train.py --data data.yaml --model yolov8n.pt --epochs 1 --imgsz 320 --batch 4
```

Si se cuenta con GPU, se puede aumentar el entrenamiento:

```bash
python src/train.py --data data.yaml --model yolov8n.pt --epochs 50 --imgsz 640 --batch 16
```

### 3. Generar predicciones

```bash
python src/predict.py --weights runs/detect/train/weights/best.pt --source datasets/mi_dataset/images/val --conf 0.25 --output evidencias/predicciones
```

Si el entrenamiento se guarda en otra carpeta, por ejemplo `train5`, se debe usar la ruta correspondiente:

```bash
python src/predict.py --weights runs/detect/train5/weights/best.pt --source datasets/mi_dataset/images/val --conf 0.25 --output evidencias/predicciones
```

## Evidencias

Las imagenes con detecciones se guardan en:

```text
evidencias/predicciones/
```

En esta carpeta se encuentran imagenes de prueba donde el modelo marca perros y gatos con bounding boxes.

## Caso de estudio: busqueda de perros y gatos desaparecidos

### Problema a resolver

En muchas comunidades es comun que perros y gatos se extravien. La busqueda normalmente depende de carteles, publicaciones en redes sociales y recorridos manuales por la zona. Este proceso puede ser lento, desorganizado y depende de que una persona reconozca visualmente al animal.

El modelo desarrollado podria utilizarse como apoyo para identificar perros y gatos en imagenes capturadas por camaras de seguridad, camaras comunitarias o fotografias enviadas por ciudadanos. De esta forma, se podria acelerar la busqueda de animales desaparecidos al detectar automaticamente la presencia de perros o gatos en distintas zonas.

### Hardware propuesto

El sistema podria integrarse con:

- Camaras de seguridad instaladas en calles, parques, veterinarias o refugios.
- Camaras domesticas o comunitarias conectadas a internet.
- Una computadora o servidor local encargado de procesar las imagenes.
- Un sistema web o aplicacion movil para consultar detecciones.
- Una base de datos con reportes de animales desaparecidos.
- Notificaciones por correo, mensaje o aplicacion cuando se detecte un posible perro o gato en una zona registrada.

### Flujo de funcionamiento

1. Una persona reporta un perro o gato desaparecido en una plataforma.
2. El sistema recibe imagenes de camaras o fotografias subidas por usuarios.
3. El modelo YOLOv8 analiza cada imagen.
4. Si detecta un perro o gato, genera una bounding box y clasifica el animal.
5. La deteccion se guarda como evidencia con fecha, hora y ubicacion aproximada.
6. El sistema compara la deteccion con reportes existentes.
7. Si existe una posible coincidencia, se envia una alerta al dueno o al refugio.
8. Las imagenes guardadas pueden revisarse manualmente para confirmar si se trata del animal desaparecido.

### Beneficios

- Acelera la busqueda de perros y gatos extraviados.
- Reduce el tiempo de revision manual de imagenes.
- Permite usar camaras ya existentes en comunidades o refugios.
- Genera evidencias visuales para confirmar posibles avistamientos.
- Puede apoyar a refugios, veterinarias y grupos de rescate animal.

### Limitaciones

- El modelo solo diferencia entre perro y gato, no identifica a un animal especifico por nombre.
- La precision puede bajar si la imagen esta borrosa, oscura o el animal aparece parcialmente.
- Para reconocer animales especificos se necesitarian mas datos, como color, tamano, raza o comparacion con imagenes del reporte.
- El sistema debe cuidar la privacidad si se usan camaras en espacios publicos o privados.

## Archivos principales del repositorio

```text
README.md
requirements.txt
data.yaml
colab_entrenamiento_yolo.ipynb
src/
datasets/
evidencias/
```

## Conclusion

El proyecto demuestra como un modelo YOLOv8 puede entrenarse para detectar perros y gatos en imagenes. Aunque el modelo es una version academica, su aplicacion puede extenderse a un sistema real de apoyo para la busqueda de mascotas desaparecidas, integrando camaras, almacenamiento de evidencias y alertas para los usuarios.
