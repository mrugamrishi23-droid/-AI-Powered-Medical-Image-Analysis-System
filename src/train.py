import os
import numpy as np
from src.preprocess import preprocess_image
from src.model import build_model

data_dir = "data/"

X = []
y = []

for label in ["NORMAL", "PNEUMONIA"]:
    folder = os.path.join(data_dir, label)
    class_num = 0 if label == "NORMAL" else 1

    for img in os.listdir(folder):
        path = os.path.join(folder, img)
        img_data = preprocess_image(path)

if img_data is not None:
    X.append(img_data)
    y.append(class_num)

X = np.array(X)
y = np.array(y)

model = build_model()

model.fit(X, y, epochs=5, batch_size=16)

model.save("models/model.keras")