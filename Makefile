#!/bin/bash

DOCKER_CONTAINERS_ID = $$(docker ps -a -q)
DOCKER_CONTAINERS_COUNT = docker ps -a -q | wc -l
DOCKER_IMAGES_ID = $$(docker images -a -q)
DOCKER_IMAGES_COUNT = $$(docker images -q | wc -l)

rm-docker-container:
	docker stop $(DOCKER_CONTAINERS_ID) 
	docker rm $(DOCKER_CONTAINERS_ID)

rm-docker-images:
	docker rmi $(DOCKER_IMAGES_ID)

run-local: rm-docker-container
	docker-compose run -d -p 8000:8000 app

list-containers:
	docker ps -a 

list-images:
	docker images -a