docker-build:
	docker-compose build

docker-up:
	docker-compose up

django-createsuperuser:
	docker exec -it seamless_django pipenv run python manage.py createsuperuser

django-makemigrations:
	docker exec -it seamless_django pipenv run python manage.py makemigrations

django-migrate:
	docker exec -it seamless_django pipenv run python manage.py migrate

django-test:
	docker exec -it seamless_django pipenv run python manage.py test
