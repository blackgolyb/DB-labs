export DOCKER_DEFAULT_PLATFORM=linux/amd64

up:
	docker compose -f docker-compose.yaml up -d

down:
	docker compose -f docker-compose.yaml down --remove-orphans