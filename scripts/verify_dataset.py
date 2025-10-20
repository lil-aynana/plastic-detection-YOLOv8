# scripts/verify_dataset_windows.py
import os

# Paths (relative to project root)
train_images = os.path.join("datasets", "combined", "train", "images")
train_labels = os.path.join("datasets", "combined", "train", "labels")
val_images = os.path.join("datasets", "combined", "val", "images")
val_labels = os.path.join("datasets", "combined", "val", "labels")

def count_files(folder, exts):
    if not os.path.exists(folder):
        return [], 0
    files = [f for f in os.listdir(folder) if f.lower().endswith(exts)]
    return files, len(files)

def check_dataset(images_path, labels_path):
    image_files, n_images = count_files(images_path, (".jpg", ".png", ".jpeg"))
    label_files, n_labels = count_files(labels_path, (".txt",))

    print(f"Checking folder: {images_path}")
    print(f"Images found: {n_images}")
    if n_images > 0:
        print(f"Sample images: {image_files[:5]}")

    print(f"Labels found: {n_labels}")
    if n_labels > 0:
        print(f"Sample labels: {label_files[:5]}")

    # Match images and labels
    missing_labels = []
    missing_images = []

    image_basenames = {os.path.splitext(f)[0] for f in image_files}
    label_basenames = {os.path.splitext(f)[0] for f in label_files}

    for img in image_basenames:
        if img not in label_basenames:
            missing_labels.append(img)
    for lbl in label_basenames:
        if lbl not in image_basenames:
            missing_images.append(lbl)

    print(f"Missing labels for images: {len(missing_labels)} -> {missing_labels[:5]}")
    print(f"Missing images for labels: {len(missing_images)} -> {missing_images[:5]}")
    print("-" * 50)

# Run checks
check_dataset(train_images, train_labels)
check_dataset(val_images, val_labels)
