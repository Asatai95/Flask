
NAME = asatai95

run:
	docker-compose build
	docker-compose up -d

stop:
	docker stop $(NAME)/docker_uwsgi
	docker stop $(NAME)/docker_nginx
	docker stop $(NAME)/docker_db

restart:
	docker restart 709f389a0e09
	docker restart 3695faf13e3c
	docker restart cbfc2460722c

rm:
	docker rm $(NAME)/docker_uwsgi
	docker rm $(NAME)/docker_nginx
