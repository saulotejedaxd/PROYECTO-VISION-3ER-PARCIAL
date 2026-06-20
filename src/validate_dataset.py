from argparse import ArgumentParser
from pathlib import Path


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


def parse_args():
    parser = ArgumentParser(description="Validar estructura basica de un dataset YOLO.")
    parser.add_argument("--dataset", required=True, help="Ruta a la carpeta del dataset.")
    return parser.parse_args()


def collect_files(folder, extensions=None):
    if not folder.exists():
        return []
    if extensions is None:
        return sorted(path for path in folder.rglob("*") if path.is_file())
    return sorted(path for path in folder.rglob("*") if path.suffix.lower() in extensions)


def check_split(dataset_path, split):
    image_dir = dataset_path / "images" / split
    label_dir = dataset_path / "labels" / split

    images = collect_files(image_dir, IMAGE_EXTENSIONS)
    labels = collect_files(label_dir, {".txt"})

    label_stems = {label.stem for label in labels}
    missing_labels = [image.name for image in images if image.stem not in label_stems]

    print(f"\nSplit: {split}")
    print(f"Imagenes encontradas: {len(images)}")
    print(f"Etiquetas encontradas: {len(labels)}")

    if missing_labels:
        print("Imagenes sin etiqueta:")
        for filename in missing_labels[:20]:
            print(f"  - {filename}")
        if len(missing_labels) > 20:
            print(f"  ... y {len(missing_labels) - 20} mas")
    else:
        print("Todas las imagenes tienen etiqueta correspondiente.")

    return len(missing_labels) == 0 and len(images) > 0


def main():
    args = parse_args()
    dataset_path = Path(args.dataset)

    if not dataset_path.exists():
        raise SystemExit(f"No existe la carpeta del dataset: {dataset_path}")

    train_ok = check_split(dataset_path, "train")
    val_ok = check_split(dataset_path, "val")

    if train_ok and val_ok:
        print("\nDataset listo para entrenamiento.")
    else:
        raise SystemExit("\nRevisa la estructura del dataset antes de entrenar.")


if __name__ == "__main__":
    main()
