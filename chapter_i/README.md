# Chapter I

## Content
- Flask
- Add endpoint ping

## Resources
- https://pnpm.io/installation

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
```

## Install Ruff
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
