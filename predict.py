
import tensorflow as tf
import numpy as np
import json
from pathlib import Path
from PIL import Image

# Get the main project folder
BASE_DIR = Path(__file__).parent

# Paths of the trained model and class names
MODEL_PATH = BASE_DIR / "models" / "cropdoc_model.keras"
CLASS_PATH = BASE_DIR / "models" / "class_names.json"

# Load the trained model
model = tf.keras.models.load_model(MODEL_PATH)

# Load disease category names
with open(CLASS_PATH, "r") as file:
    class_names = json.load(file)

# Ask the user for a leaf image path
image_path = input("Enter the image path: ")

# Open and prepare the image
image = Image.open(image_path).convert("RGB")
image = image.resize((160, 160))

# Convert image into a NumPy array
image_array = np.array(image)

# Add batch dimension
image_array = np.expand_dims(image_array, axis=0)

# Predict the disease
predictions = model.predict(image_array)

# Find the category with the highest score
predicted_index = np.argmax(predictions[0])
predicted_class = class_names[predicted_index]

# Calculate confidence score
confidence = predictions[0][predicted_index] * 100

# Display the result
print("\n----- CropDoc AI Result -----")
print("Predicted Disease:", predicted_class)
print("Confidence:", round(float(confidence), 2), "%")
