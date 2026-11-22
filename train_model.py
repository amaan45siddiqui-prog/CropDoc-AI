import tensorflow as tf
import json
from pathlib import Path

# Project folders
BASE_DIR = Path(__file__).parent

DATASET_PATH = (
    BASE_DIR / "dataset" / "PlantVillage-Dataset-master"
    / "raw" / "color"
)

MODEL_PATH = BASE_DIR / "models"
MODEL_PATH.mkdir(exist_ok=True)


# Image settings
IMAGE_SIZE = (160, 160)
BATCH_SIZE = 16

# Load training images
train_data = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,    
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE
)

# Load validation images
validation_data = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE
)

class_names = train_data.class_names
print("Total categories:", len(class_names))
print("Categories:", class_names)

# Improve data loading speed
AUTOTUNE = tf.data.AUTOTUNE

train_data = train_data.prefetch(buffer_size=AUTOTUNE)
validation_data = validation_data.prefetch(buffer_size=AUTOTUNE)

# Load pretrained MobileNetV2
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(160, 160, 3),
    include_top=False,
    weights="imagenet"
)

# Freeze pretrained layers
base_model.trainable = False

# Build our classification model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(160, 160, 3)),
    tf.keras.layers.Rescaling(1./127.5, offset=-1),
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(len(class_names), activation="softmax")
])

# Compile model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Display model architecture
model.summary()

# Train model
history = model.fit(
    train_data,
    validation_data=validation_data,
    epochs=5
)

# Save trained model
model.save(MODEL_PATH / "cropdoc_model.keras")

# Save category names
with open(MODEL_PATH / "class_names.json", "w") as file:
    json.dump(class_names, file)

print("\nModel training completed successfully!")
print("Model saved in the models folder.")