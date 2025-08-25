## docker management

build:
	docker compose build

docker-up:
	docker compose up -d

up: build docker-up

down:
	docker compose down

volumes: 
	docker volume ls

restart:
	docker compose down -v  # Remove containers and volumes
	docker compose up -d --build  # Start fresh, this will trigger data re-initialization

sh:
	docker exec -it dbt_core /bin/bash