docker-build:
	docker-compose build

docker-up:
	docker-compose up

django-test:
	docker exec -it django pipenv run python manage.py test