from fastapi import FastAPI, UploadFile, File
import uvicorn
import numpy as np
import tensorflow as tf

from utils import read_file_as_image

app = FastAPI()

model_verison = 6
MODEL = tf.keras.models.load_model(f"../training/saved-models/models/{model_verison}")
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]  # As defined in the training notebook


@app.get("/ping")
async def ping():
    return "Hello, I am alive"


@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    """
    Upload a file to the api and get a prediction
    Args:
        file: A file that can be uploaded and used in the payload of the request

    Returns:

    """
    # The await is to allow multiple requests to read the file without stopping here
    image = read_file_as_image(await file.read())

    # Let's make the image into a batch
    img_batch = np.expand_dims(image, 0)

    predictions = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8080)
