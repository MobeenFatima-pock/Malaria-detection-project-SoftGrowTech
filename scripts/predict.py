
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

def predict_image(model_path, img_path):
    model = load_model(model_path)
    img = image.load_img(img_path, target_size=(64,64))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    pred = model.predict(img_array)
    return pred[0][0]

if __name__ == "__main__":
    model_file = os.path.join("model", "malaria_model.h5")
    test_image = os.path.join("dataset", "cell_images", "Parasitized", "cell_1.png")
    pred = predict_image(model_file, test_image)
    print("Prediction (probability of infected):", pred)
