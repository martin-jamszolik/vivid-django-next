# Developer Guide

Welcome developer, happy to have you here!. This guide will help you get
started with our application so you can be productive in no time.

## Database setup

See [MAIN README](../README.md#database-postgres-setup)


## Python Setup

See [MAIN README](../README.md#django-backend-setup)

## Running backend

```sh
# Make sure your database is all up to date
python manage.py migrate
# Run the Embedded Server
python manage.py runserver
```

If you would like to interact with the Database models, you can use django `shell` to do that.

```sh
python manage.py shell
```
```python
# Using Python Interpreter
Proposal.objects.all()
```
Checkout Django Tutorial for all the cool Model features available at [Tutorial Documentation](https://docs.djangoproject.com/en/4.1/intro/tutorial02/)

Django admin site is really useful, so don't forget to set that up too. [Django Admin](https://docs.djangoproject.com/en/4.1/intro/tutorial02/#introducing-the-django-admin)