import numpy as np
from tensorflow.keras.models import load_model
from src.preprocess import preprocess_image

model = load_model("models/model.h5")

def predict(image_path):
    img = preprocess_image(image_path)
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    return "PNEUMONIA" if prediction[0][0] > 0.5 else "NORMAL"