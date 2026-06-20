from argparse import ArgumentParser
from pathlib import Path

from ultralytics import YOLO


def parse_args():
    parser = ArgumentParser(description="Generar predicciones y guardar evidencias con bounding boxes.")
    parser.add_argument("--weights", required=True, help="Ruta al archivo best.pt entrenado.")
    parser.add_argument("--source", required=True, help="Imagen, carpeta, video o camara para probar.")
    parser.add_argument("--conf", type=float, default=0.25, help="Umbral minimo de confianza.")
    parser.add_argument("--output", default="evidencias/predicciones", help="Carpeta de salida.")
    return parser.parse_args()


def main():
    args = parse_args()
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)

    model = YOLO(args.weights)
    model.predict(
        source=args.source,
        conf=args.conf,
        save=True,
        project=str(output.parent),
        name=output.name,
        exist_ok=True,
    )

    print(f"Evidencias guardadas en: {output}")


if __name__ == "__main__":
    main()
