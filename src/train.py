from argparse import ArgumentParser

from ultralytics import YOLO


def parse_args():
    parser = ArgumentParser(description="Entrenar un modelo YOLO con Ultralytics.")
    parser.add_argument("--data", default="data.yaml", help="Ruta al archivo data.yaml.")
    parser.add_argument("--model", default="yolov8n.pt", help="Modelo base: yolov8n.pt, yolov8s.pt, etc.")
    parser.add_argument("--epochs", type=int, default=50, help="Numero de epocas de entrenamiento.")
    parser.add_argument("--imgsz", type=int, default=640, help="Tamano de imagen para entrenamiento.")
    parser.add_argument("--batch", type=int, default=16, help="Tamano de batch.")
    parser.add_argument("--project", default="runs/detect", help="Carpeta donde se guardan resultados.")
    parser.add_argument("--name", default="train", help="Nombre del experimento.")
    return parser.parse_args()


def main():
    args = parse_args()
    model = YOLO(args.model)
    model.train(
        data=args.data,
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        project=args.project,
        name=args.name,
    )


if __name__ == "__main__":
    main()
