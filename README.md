# Demo for users location web application
This application uses Django 4.2 as a Framework. For the interface, Argon admin template and Bootstrap have been integrated into the code. The are used for the login/register and main pages which are User location map, profile and profile edition.

Docker is required to start the application. Get docker here: https://docs.docker.com/get-docker/. For GNU/Linux OS based, docker engine is prefered.

It has been dockerized to facilitate its startup and to be a standalone app. There are two docker services running which are `web` for Django and `db` for the PostGIS database.

## Quick start

### 1. Generate the .env file from env.example
Since some parameters are confidential, using an .env to access them is mandatory.
```sh
$ cp env.example .env
# Edit the .env file with your prefered editor and 
# put your database parameters. You can also use the defaults
# values.
```

### 2. Build and run the server
To run the app server with docker, the first step is building it. The run all commands listed in the `Dockerfile` such as requirements installation.
```sh
$ docker compose build
$ docker compose up # You can add -d option to run it in background and type docker compose down to stop it.
```

### 3. Create a Super User
This part is mandatory if you want to access to the django admin page which can't be accessed by simple users created from register page.
```sh
$ docker compose exec web python manage.py createsuperuser
```

### 4. Open the app on a web browser
Open a web browser and navigate to http://localhost:8000 to log in or register a new user.

Navigate to http://localhost:8000/admin to access (as an admin user) to the Django administration page. 

## Usefull commands

### Create migration and migrate to the DB
If you add or edit a model, you can do a migration by running the following commands.
```sh
$ docker compose exec web python manage.py makemigrations
$ docker compose exec web python manage.py migrate
```

## Run test cases
Test cases are a fundamental part of the development because they contribute to the overall quality, reliability, and maintainability of the application. They help catch and prevent issues, document the code, and provide confidence in development process, ultimately leading to a more robust and successful project.

You can run unit tests using the following comands. These test automatically run each time when a pull request is open on the branch `main`. On GitHub, you can access to it in your pull request check tab.

Currently, there are 14 test cases in the entire app relative to login, profile view, profile editing, map view and new user registration. You can run all of them in one time or one by one.
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
