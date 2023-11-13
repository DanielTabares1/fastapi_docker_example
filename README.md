# fastapi_docker_example
Se desarrollará una API en Python, con FastAPI y PostgreSQL con todo montado en docker bien bonito :3 

### Para ejecutar el proyecto (Esto no sirve de momento, toca crear la base de datos aparte y luego correr el proyecto localmente)
Lo primero es buildear las imágenes de docker, simplemente necesita una terminal en la raíz del proyecto y ejecutar el siguiente comando.  
```
docker-compose up -d
```

y ya puede acceder a la api por http://localhost:8080 .   
y para ver la **documentación** http://localhost:8080/docs o http://localhost:8008/redoc .

La base de datos aún no es visible, la puede modificar desde el contenedor pero próximamente organizaré eso
