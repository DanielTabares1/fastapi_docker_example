# fastapi_docker_example
Se desarrollará una API en Python, con FastAPI y PostgreSQL con todo montado en docker bien bonito :3 

### Para ejecutar el proyecto
Lo primero es buildear la imagen de docker, simplemente necesita una terminal en la raíz del proyecto y ejecutar el siguiente comando.  
```
docker build -t fastapi-docker .
```
Lo siguiente sería crear un contenedor de docker basado en dicha imagen
```
docker run -d -p 8080:80 fastapi-docker
```

y finalmente, acceder a la api por http://localhost:8080 .   
y para ver la **documentación** http://localhost:8080/docs o http://localhost:8008/redoc .  
