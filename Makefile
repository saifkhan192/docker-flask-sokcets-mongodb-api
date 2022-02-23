
build:
	cp -u .env.dist .env
	docker-compose --file docker/docker-compose.yml up -d --force-recreate --no-deps --build

up:
	docker-compose --file docker/docker-compose.yml up

recreate_all:
	# docker-compose --file docker/docker-compose.yml up -d --force-recreate --no-deps --build mongodb
	docker-compose --file docker/docker-compose.yml up -d --force-recreate --no-deps --build flask_app

run_all:
	docker container start mongodb || true
	docker container start flask_app || true
	# sleep 2
	# google-chrome http://localhost

stop_all:
	docker container stop mongodb || true
	docker container stop flask_app || true

refresh_app:
	make clear_cache
	docker-compose --file docker/docker-compose.yml up --force-recreate --no-deps flask_app

bash_app:
	@docker exec -it flask_app /bin/bash

chrome_debug:
	/usr/bin/google-chrome http://localhost:3001 --remote-debugging-port=9222 --no-first-run --no-default-browser-check --user-data-dir=/home/saifullah/Desktop/vscode-chrome

run_app:
	docker-compose --file docker/docker-compose.yml up -d flask_app
	docker-compose --file docker/docker-compose.yml up -d mongodb
	sleep 1
	google-chrome http://localhost/socket-frontend

follow_logs:
	docker logs --follow flask_app

git_push:
	git push origin master
	notify-send "Done"

print_docker_env:
	@docker-compose --file docker/docker-compose.yml run flask_app printenv

run_tests:
	docker exec -it flask_app pytest

run_tests_with_details:
	docker exec -it flask_app pytest -v

clear_cache:
	sudo rm -rf __pycache__ && sudo rm -rf docker/py_cache && sudo rm -rf *.pyc && sudo rm -rf __pycache__