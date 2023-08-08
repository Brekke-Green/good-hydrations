build:
	docker compose up -d --build

debug:
	docker compose up --build

close:
	docker compose down

.PHONY: build debug close
