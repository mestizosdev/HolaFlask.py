# Chapter VII

## Content
- Test

## [Database](./DATABASE.md)
Create database test for testing
```
create database test;
```
## Install MailHog on docker
Go to MailHog folder and run
```
docker build -t mailhog .
```
```
docker run -d --name mailhog -p 8025:8025 -p 1025:1025 mailhog
```
```
docker logs mailhog
```
### Go to http://localhost:8025/ to see the mailhog interface

## Install dependencies
```
virtualenv -p python3.12 venv
```
```
source venv/bin/activate
```
```
pip install -U pip
pip install --upgrade wheel
pip install --upgrade setuptools
```
```
pip install -r requirements.txt
```

## Migrations
```
flask --app flaskr db init
flask --app flaskr db migrate
flask --app flaskr db upgrade
```
### Undo upgrade migrate
```
flask --app flaskr db downgrade
```
### Remove migration folder for new migration
```
rm -rf migrations
```
## Seed database
```
flask --app flaskr seed
```
### Undo seed
```
flask --app flaskr unseed
```
## Test
Run
```
pytest
```
Run with print
```
pytest -s
```

## Run
```
flask --app flaskr run --debug
```

