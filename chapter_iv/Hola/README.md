# Chapter III

## Content
- Seeding in database with initial data

## Resources
- https://insomnia.rest

## Install dependencies
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
### Remove migration folder for new migration (optional)
```
rm -rf migrations
```

## Run
```
flask --app flaskr run --debug
```

