build:
	docker compose up -d --build

build_debug:
	docker compose up --build

close:
	docker compose down

.PHONY: build build_debug close
