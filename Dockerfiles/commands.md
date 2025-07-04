docker build -f Dockerfiles/Dockerfile.3.5.2 -t p352 . --progress=plain
docker build -f Dockerfiles/Dockerfile.3.10 -t p310 . --progress=plain
docker build -f Dockerfiles/Dockerfile.3.11 -t p311 . --progress=plain
docker build -f Dockerfiles/Dockerfile.3.12 -t p312 . --progress=plain
docker run -it p352
docker run -it p310
docker run -it p311
docker run -it p312
