start:
	docker-compose up

stop:
	docker-compose down

migrate:
	docker-compose run django python manage.py migrate