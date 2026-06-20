# Deteccion de perros y gatos con YOLO

## Integrantes

- Nombre del integrante 1: **TU NOMBRE**
- Nombre del integrante 2: **NOMBRE DE TU COMPANERO/A**  
  Si el trabajo es individual, elimina esta linea.

## Descripcion del proyecto

Este proyecto aplica conceptos de Vision Artificial mediante el entrenamiento de un modelo de la familia YOLO para detectar y diferenciar perros y gatos en imagenes. El repositorio contiene scripts para preparar datos, entrenar el modelo, probarlo con imagenes nuevas y guardar evidencias con bounding boxes.

## Estructura del repositorio

```text
.
+-- README.md
+-- requirements.txt
+-- data.yaml
+-- src/
|   +-- train.py
|   +-- predict.py
|   +-- validate_dataset.py
+-- datasets/
|   +-- README.md
+-- evidencias/
    +-- README.md
```

## Requisitos

- Python 3.10 o superior
- Git
- Cuenta de GitHub
- Dataset etiquetado en formato YOLO

## Instalacion

### Opcion A: Google Colab

1. Sube esta carpeta a Google Drive.
2. Abre el notebook `colab_entrenamiento_yolo.ipynb`.
3. Activa GPU en Colab:

```text
Entorno de ejecucion > Cambiar tipo de entorno de ejecucion > GPU
```

4. Ejecuta las celdas en orden.
5. Al finalizar, descarga o guarda las evidencias generadas en `evidencias/predicciones/`.

### Opcion B: Computadora local

1. Clonar el repositorio:

```bash
git clone URL_DE_TU_REPOSITORIO
cd NOMBRE_DEL_REPOSITORIO
```

2. Crear un entorno virtual:

```bash
python -m venv .venv
```

3. Activar el entorno virtual:

En Windows:

```bash
.venv\Scripts\activate
```

En macOS/Linux:

```bash
source .venv/bin/activate
```

4. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Preparacion del dataset

Este repositorio ya incluye un dataset combinado en formato YOLOv8 para detectar perros y gatos:

- Entrenamiento: 522 imagenes.
- Validacion: 82 imagenes.
- Clases finales:
  - `0`: perro
  - `1`: gato

El dataset esta en esta estructura:

```text
datasets/mi_dataset/
+-- images/
|   +-- train/
|   +-- val/
+-- labels/
    +-- train/
    +-- val/
```

Cada imagen debe tener un archivo `.txt` con el mismo nombre dentro de `labels`. Cada linea del archivo de etiquetas usa el formato:

```text
clase x_centro y_centro ancho alto
```

Las coordenadas deben estar normalizadas entre 0 y 1.

Antes de entrenar, editar `data.yaml` con:

- Ruta del dataset.
- Numero de clases.
- Nombre de las clases.

Ejemplo:

```yaml
path: datasets/mi_dataset
train: images/train
val: images/val
names:
  0: perro
  1: gato
```

## Validar dataset

Para revisar que las imagenes tengan etiquetas correspondientes:

```bash
python src/validate_dataset.py --dataset datasets/mi_dataset
```

## Entrenamiento del modelo

Para entrenar YOLOv8:

```bash
python src/train.py --data data.yaml --model yolov8n.pt --epochs 50 --imgsz 640
```

El entrenamiento genera resultados en:

```text
runs/detect/
```

El archivo principal del modelo entrenado normalmente queda en:

```text
runs/detect/train/weights/best.pt
```

## Pruebas con imagenes nuevas

Para probar el modelo con imagenes:

```bash
python src/predict.py --weights runs/detect/train/weights/best.pt --source datasets/mi_dataset/images/val --conf 0.25
```

Las imagenes con bounding boxes se guardan en:

```text
evidencias/predicciones/
```

## Caso de estudio: aplicacion practica en la industria

### Problema a resolver

En refugios, veterinarias o centros de monitoreo animal, puede ser necesario identificar automaticamente si en una zona aparece un perro o un gato. La revision manual de camaras puede tomar mucho tiempo, especialmente si hay varias jaulas, patios o areas de observacion. El objetivo del sistema es usar una camara y un modelo YOLO entrenado para detectar perros y gatos en tiempo real.

### Hardware propuesto

El sistema propuesto estaria compuesto por:

- Una camara RGB instalada en una jaula, patio, pasillo o zona de observacion.
- Iluminacion LED constante para evitar sombras y variaciones fuertes de luz.
- Una computadora, Jetson Nano, Raspberry Pi con acelerador o PC con GPU para ejecutar el modelo YOLO.
- Un sistema de registro conectado a una base de datos o panel de monitoreo.
- Una alarma, notificacion o sistema de apertura/cierre automatico si se requiere separar animales por zona.

### Flujo de funcionamiento

1. La camara captura imagenes o video de la zona de observacion.
2. La imagen se envia al procesador donde esta cargado el modelo YOLO entrenado.
3. YOLO detecta perros y gatos y genera bounding boxes con una confianza.
4. Si la confianza supera el umbral definido, el sistema registra la deteccion.
5. El sistema puede mostrar la deteccion en un panel, guardar evidencia o enviar una alerta.
6. En un caso mas avanzado, podria activar una puerta automatica para separar areas segun el tipo de animal.
7. Las detecciones se guardan para auditoria, conteo de animales y mejora futura del modelo.

### Beneficios esperados

- Identificacion automatica de perros y gatos.
- Monitoreo mas rapido de zonas con varios animales.
- Evidencia visual de los resultados.
- Posibilidad de operar en tiempo real.
- Mejora continua al recolectar nuevas imagenes del proceso.

### Limitaciones

- El modelo depende de la calidad y variedad del dataset.
- Cambios de iluminacion, angulo de camara, fondo o postura del animal pueden afectar el rendimiento.
- Es necesario reentrenar el modelo si se agregan nuevas clases o si el entorno cambia mucho.

## Evidencias

La carpeta `evidencias/` debe contener imagenes o videos generados por el modelo donde se observen las detecciones con bounding boxes.

Ejemplos esperados:

- `evidencias/predicciones/imagen_001.jpg`
- `evidencias/predicciones/imagen_002.jpg`
- `evidencias/video_prueba.mp4`

## Entrega en Classroom

Ambos integrantes deben enviar exactamente la misma URL del repositorio de GitHub:

1. Entrar a Classroom.
2. Ir a "Tu trabajo".
3. Seleccionar "Anadir o crear".
4. Elegir "Enlace".
5. Pegar la URL del repositorio compartido.
6. Hacer clic en "Entregar".
