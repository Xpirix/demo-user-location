# Demo for users location web application
This application uses Django 4.2 as a Framework. 

It has been dockerized to facilitate its startup. There are two docker services running which are `web` for Django and `db` for the PostGIS database.

## Quick start

### 1. Generate the .env file from env.example
```sh
$ cp env.example .env
# (Optional) Edit the .env file with your prefered editor and put your database parameters
$ nano .env
```

### 2. Build and run the server server
```sh
$ docker compose build
$ docker compose up
```

### 3. Create a Super User
```sh
$ docker compose exec web python manage.py createsuperuser
```