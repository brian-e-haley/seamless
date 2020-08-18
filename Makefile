docker-build:
	docker-compose build

docker-up:
	docker-compose up

django-createsuperuser:
	docker exec -it seamless_django pipenv run python manage.py createsuperuser

django-dumpdeta:
	docker exec -it seamless_django pipenv run python manage.py dumpdata --format=json patients > patients/fixtures/patient.json

django-loadjson:
	docker exec -it seamless_django pipenv run python manage.py loadjson --settings=seamless.settings.production

django-makemigrations:
	docker exec -it seamless_django pipenv run python manage.py makemigrations

django-migrate:
	docker exec -it seamless_django pipenv run python manage.py migrate --settings=seamless.settings.production

django-shell:
	docker exec -it seamless_django pipenv run python manage.py shell

django-flush:
	docker exec -it seamless_django pipenv run python manage.py flush --settings=seamless.settings.production

django-test:
	docker exec -it seamless_django pipenv run python manage.py test
