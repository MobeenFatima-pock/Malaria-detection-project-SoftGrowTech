# Malaria-detection-project-SoftGrowTech
This project implements a Convolutional Neural Network (CNN) to detect malaria-infected blood cells from microscopic images.
# Malaria Detection Project

## Overview

This project is a **Malaria Cell Image Detection System** using Convolutional Neural Networks (CNN) built with **TensorFlow 2.x** and deployed with **Flask**. It classifies blood cell images as either **Parasitized** or **Uninfected**.

## Folder Structure

```
MALARIA_DETECTION_PROJECT/
├─ dataset/                  # Contains cell images for training/validation
│  └─ cell_images/
│     ├─ Parasitized/
│     └─ Uninfected/
├─ model/                    # Stores trained models
├─ scripts/                  # Python scripts
│  ├─ train_model.py         # Trains CNN model
│  ├─ evaluate_model.py      # Evaluates model on validation data
│  └─ predict.py             # Predicts on single images
├─ static/upload/            # Upload folder for Flask app
├─ templates/index.html      # HTML template for web app
├─ app.py                    # Flask application
└─ requirements.txt          # Dependencies
```

## Installation

1. Clone or extract the ZIP folder to a local directory outside OneDrive.
2. Navigate to the project folder:

```bash
cd MALARIA_DETECTION_PROJECT
```

3. Create a virtual environment (recommended):

```bash
python -m venv venv
```

4. Activate the virtual environment:

* Windows:

```bash
venv\Scripts\activate
```

* macOS/Linux:

```bash
source venv/bin/activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Train the Model

```bash
python scripts/train_model.py
```

* Generates `malaria_model.h5` in the `model/` folder.

### 2. Evaluate the Model

```bash
python scripts/evaluate_model.py
```

* Outputs validation accuracy and loss.

### 3. Predict a Single Image

```bash
python scripts/predict.py
```

* Uses a sample image in `dataset/cell_images/Parasitized` to test prediction.

### 4. Run the Web App

```bash
python app.py
```

* Opens Flask web app at `http://127.0.0.1:5000/`
* Upload an image to get prediction: `Parasitized` or `Uninfected`.

## Notes

* Ensure **dataset images** are properly placed in `dataset/cell_images/Parasitized` and `Uninfected`.
* All scripts and Flask app use **relative paths** to avoid errors.
* Running outside **OneDrive** prevents path-related issues.

## Contact

For any questions, contact: **[Your Name]**

* GitHub: https://github.com/MobeenFatima-pock
* LinkedIn: www.linkedin.com/in/mobeen-fatima-599a35347


