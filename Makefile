start:
	docker-compose up

stop:
	docker-compose down

makemigrations:
	docker-compose run django python manage.py makemigrations

migrate:
	docker-compose run django python manage.py migrate

test:
	docker-compose run django python manage.py test

