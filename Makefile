build:
	docker compose up -d --build

close:
	docker compose down

.PHONY: build close
