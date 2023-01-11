

# Full Stack Guide

Welcome to our full stack app `vivid`. Using Django and NextJS as one cohesive application. From zero to your first PR.

## Database Postgres Setup

```sh
docker-compose up -d db
```

## Django backend Setup

```sh
cd backend
python3 -m venv .venv
source .venv/bin/activate

# Install and dependencies
python3 -m pip install -r requirements.txt

#Prepare your .env file for local values
cp .env.sample .env
```

For more instructions see backend [README.md](backend/README.md)

## NextJS frontend Setup

```sh
# TODO
```

## Devops (CI/CD)

[README.md](devops/README.md)