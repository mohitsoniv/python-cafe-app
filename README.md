# python-cafe-app with Mohit Soni (mohitsoniv)
## 1. Create a docker image
```
docker build -t my-cafe-app:menu .
```
## 2. Create a docker container 
```
docker run -it my-cafe-app:menu

docker run -itd -P my-cafe-app:menu
```
