# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY ./requirements-api.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements-api.txt

# Copy the FastAPI application code into the container
COPY . /app/

# Expose the port on which the FastAPI server will run (change as needed)
EXPOSE ${PORT}

# Command to run the FastAPI server
CMD ["sh", "-c", "uvicorn main-tf-serving:app --host $HOST --port $PORT"]
