## Build the docker image
```bash
docker build -t flask-docker-app
```

## Run container
```bash
docker run -p 5000:5000 flask-docker-app
```

## If port is in-use run
```bash
docker run -p 5001:5000 flask-docker-app
```

## Open Application on Browser
http://127.0.0.1:5001/
