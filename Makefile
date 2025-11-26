.PHONY: help run install test build


help:
	@echo "Available commands:"
	@echo ""
	@echo "Local Development:"
	@echo "  build		- Crea un contenedor con el servidor"
	@echo "  run		- Ejecuta el servidor en contenedor"
	@echo "  test		- Ejecuta los casos de prueba localmente"
	@echo "  up			- crea y ejecuta el servidor en un contenedore"
	@echo " test-docker	- Ejecuta los test cases dentro del un contenedor"
build:
	docker build -f Dockerfile . -t savant

run:
	docker run -p 8100:8100 savant:latest

test:
	pytest

test-docker:
	docker run --rm \
		-v $(shell pwd)/reports:/app/reports \
		savant \
		sh -c "uvicorn main:app --host 0.0.0.0 --port 8100 & sleep 100 && pytest"


up: build run