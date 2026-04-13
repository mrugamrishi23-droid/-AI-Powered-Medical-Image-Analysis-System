import cv2
import numpy as np

IMG_SIZE = 224

def preprocess_image(path):
    img = cv2.imread(path)

    if img is None:
        return None   # skip bad images

    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    return img