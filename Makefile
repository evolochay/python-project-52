LOCAL := poetry run python manage.py

install:
	poetry install

uninstall:
	python3 -m pip uninstall hexlet-code

lint:
	poetry run flake8 task_manager

test:
	$(LOCAL) test --traceback -v 2

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage xml
	poetry run coverage report

# make test-coverage:
# 	poetry run pytest --cov=task_manager --cov-report xml tests/

messages:
	poetry run django-admin makemessages -l ru

compilemess:
	poetry run django-admin compilemessages

server:
	$(LOCAL) runserver

migrations:
	$(LOCAL) makemigrations
migrate:
	$(LOCAL) migrate
