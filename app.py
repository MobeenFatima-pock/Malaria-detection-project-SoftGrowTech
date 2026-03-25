
import os
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

model_path = os.path.join("model", "malaria_model.h5")
upload_folder = os.path.join("static", "upload")
os.makedirs(upload_folder, exist_ok=True)

model = load_model(model_path)

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(64,64))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    pred = model.predict(img_array)
    return pred[0][0]

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    prob = None
    if request.method == "POST":
        file = request.files["image"]
        if file:
            filepath = os.path.join(upload_folder, file.filename)
            file.save(filepath)
            pred_val = predict_image(filepath)
            prediction = "Parasitized" if pred_val > 0.5 else "Uninfected"
            prob = pred_val
    return render_template("index.html", prediction=prediction, prob=prob)

if __name__ == "__main__":
    app.run(debug=True)
