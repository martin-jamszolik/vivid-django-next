# Developer Guide

Welcome developer, happy to have you here!. This guide will help you get
started with our application so you can be productive in no time.

## Database setup

```sh
cd ..
docker-compose up -d db
```
As explained in the [main readme](../README.md#database-postgres-setup)


## Django Setup

As explained in the [main readme](../README.md#django-backend-setup)

Again, make sure you have reviewed you local `.env` before you start

## Running backend

```sh
# When you have new model changes
python manage.py makemigrations

# Make sure your database is all up to date
python manage.py migrate

# Run the Embedded Server
python manage.py runserver
```

Add some records using django `shell`.

```sh
python manage.py shell
```
```python
# Using Python Interpreter
from estimations.models import Project, Proposal
Project.objects.all()
Project.objects.create(name="shellTest1", status="Draft")
```
Checkout Django Tutorial for all the cool Model features available at [Tutorial Documentation](https://docs.djangoproject.com/en/4.1/intro/tutorial02/)

Django admin site to setup an authenticated user. [Django Admin](https://docs.djangoproject.com/en/4.1/intro/tutorial02/#introducing-the-django-admin)