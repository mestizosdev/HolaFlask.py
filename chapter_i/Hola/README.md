# Chapter I

## Resources
- https://httpie.io

## Content
- Flask
- Add endpoint ping

## Resources
- https://flask.palletsprojects.com
- https://github.com/astral-sh/ruff

## Create folders and files
```
mkdir flaskr
touch flaskr/__init__.py
touch pyproject.toml
```

## Create python virtual environment
```
virtualenv venv
```
or
```
virtualenv -p python3.11 venv
```
## Activate python virtual environment
```
source venv/bin/activate
```
## Update pip and tools
```
pip install -U pip
pip install --upgrade wheel
pip install --upgrade setuptools
```

## Install Flask
```
pip install Flask
pip install Flask-RESTful
```
## Install linter and code formatter (Ruff)
```
pip install ruff
```
### Check syntax
```
ruff check .
```
### Format
```
ruff format .
```

## Run
```
flask --app flaskr run --debug
```

