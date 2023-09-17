# Demo for users location web application
This application uses Django 4.2 as a Framework.

Docker is required to start the application. Get docker here: https://docs.docker.com/get-docker/. For GNU/Linux OS based, docker engine is prefered.

It has been dockerized to facilitate its startup and to be a standalone app. There are two docker services running which are `web` for Django and `db` for the PostGIS database.

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

### 4. Open the app on a web browser
Open a web browser and navigate to http://localhost:8000 to log in or register a new user.

Navigate to http://localhost:8000/admin for log in to the Django administration page. 

## Usefull commands

### Create migration and migrate to the DB
```sh
$ docker compose exec web python manage.py makemigrations
$ docker compose exec web python manage.py migrate
```

## Run test cases
You can run unit tests using the following comands:
### Run all tests
```sh
$ docker compose exec web python manage.py test
```
### Test login
```sh
$ docker compose exec web python manage.py test appUsers.tests.LoginTestCase
```
### Test Profile
```sh
$ docker compose exec web python manage.py test appUsers.tests.ProfileViewTestCase
```
### Test Profile Edit
```sh
$ docker compose exec web python manage.py test appUsers.tests.EditProfileViewTestCase
```
### Test Users map
```sh
$ docker compose exec web python manage.py test appUsers.tests.UsersMapViewTestCase
```
### Test Register a new user
```sh
$ docker compose exec web python manage.py test appUsers.tests.SignupViewTestCase
```
