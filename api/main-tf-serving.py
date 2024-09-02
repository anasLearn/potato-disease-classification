import os
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
import requests
from dotenv import load_dotenv

from utils import read_file_as_image

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TF serving endpoint
TF_SERVING_CONTAINER = os.environ.get("TF_SERVING_HOST")
TF_SERVING_PORT = os.environ.get("TF_SERVING_PORT", default="8605")
tf_serving_endpoint = f"http://{TF_SERVING_CONTAINER}:{TF_SERVING_PORT}/v1/models/potato-model:predict"  # This indicates the latest version

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

    # The payload of the post request to TF-serving API must be as follow
    json_data = {
        "instances": img_batch.tolist()
    }

    response = requests.post(tf_serving_endpoint, json=json_data)
    prediction = response.json()["predictions"][0]

    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = np.max(prediction)
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8080)
