# Chapter II

## Content
- Add endpoint version

## Install dependencies
```
pip install Flask-SQLAlchemy
pip install psycopg
pip install Flask-Cors
```

## Run
```
flask --app flaskr run --debug
```

## Resolving error
```
from flaskr import app
ImportError: cannot import name 'app' from partially initialized module 'flaskr' (most likely due to a circular import)
```
