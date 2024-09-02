#!/bin/bash

# List of containers to delete
containers=(
    predict-api-container
    tf-serving-container
    
)

# List of images to delete
images=(
    predict-api-image
)

# List of volumes to delete
volumes=(
    
)

# Delete containers
echo "Deleting containers..."
for container in "${containers[@]}"; do
    if docker ps -a | grep -q "$container"; then
        docker rm -f "$container"
        echo "Deleted container: $container"
    else
        echo "Container not found: $container"
    fi
done

# Delete images
echo "Deleting images..."
for image in "${images[@]}"; do
    if docker images | grep -q "$image"; then
        docker rmi -f "$image"
        echo "Deleted image: $image"
    else
        echo "Image not found: $image"
    fi
done

# Delete volumes
echo "Deleting volumes..."
for volume in "${volumes[@]}"; do
    if docker volume ls | grep -q "$volume"; then
        docker volume rm "$volume"
        echo "Deleted volume: $volume"
    else
        echo "Volume not found: $volume"
    fi
done

# Run the docker compose command
echo "Running docker compose..."
docker compose -p leaf-classifier -f TensorFlow-Serving-API/docker-compose.yml  up  -d
docker compose -p leaf-classifier -f api/docker-compose.yml  up --build -d

# docker compose -p leaf-classifier -f TensorFlow-Serving-API/docker-compose.yml    -f api/docker-compose.yml  up --build -d


echo "Script completed."
