# Image Classification API

This repository provides an API to interact with the trained model, allowing users to post images and receive classification results.

We have implemented two options for serving the API:

1. **[FastAPI](./main.py)**: Directly access the model to make predictions.
2. **[TensorFlow Serving](./main-tf-serving.py)**: Run TensorFlow Serving container with the chosen models and build a FastAPI app that connects to it.

## TensorFlow Serving, Explanation and Setup

Refer to the [TensorFlow Serving API guide](../TensorFlow-Serving-API/README.md).

## Run the api

Whether running the api locally or in a docker container with docker compose, you will need to create the `.env` file to define the environment variables.
Do that by copying the content of `sample.env` into `.env` and modifying it as needed.
