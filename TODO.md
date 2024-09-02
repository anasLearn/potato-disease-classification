* Check why this line doesn't work:
```
docker compose -p leaf-classifier -f TensorFlow-Serving-API/docker-compose.yml  -f api/docker-compose.yml  up --build -d
```