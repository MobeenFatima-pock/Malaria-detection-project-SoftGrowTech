
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

val_dir = os.path.join("dataset", "cell_images")
model_path = os.path.join("model", "malaria_model.h5")

model = load_model(model_path)

val_datagen = ImageDataGenerator(rescale=1./255)
val_generator = val_datagen.flow_from_directory(val_dir, target_size=(64,64), batch_size=32, class_mode='binary', shuffle=False)

loss, accuracy = model.evaluate(val_generator)
print(f"Validation Loss: {loss:.4f}, Accuracy: {accuracy:.4f}")
