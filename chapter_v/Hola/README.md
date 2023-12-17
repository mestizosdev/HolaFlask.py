# Chapter V

## Content
- Login

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

## Run
```
flask --app flaskr run --debug
```

