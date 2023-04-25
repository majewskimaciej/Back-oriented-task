# Back-oriented-task

- To start the server first create the Docker image of the application.
- Go to the directory with the Dockerfile and run this command to build the image:
```
docker-compose build
```
- Then run this command to start the server:
```
docker-compose up
```

- To query operation 1, run this command, which should return: {"average":4.0424}
```
curl http://localhost:8000/average/USD/2022-01-03
```

- To query operation 2, run this command, which should return: {"min":4.1649,"max":5.0381}
```
curl http://localhost:8000/minmax/USD/255
```

- To query operation 3, run this command, which should return:{"major":0.1004}
```
curl http://localhost:8000/difference/USD/255
```

- To use the Swagger-UI frontend go to this url:
```
http://localhost:8000/docs
```