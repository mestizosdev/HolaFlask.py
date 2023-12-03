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
pip install Flask-RESTful
pip install Flask-SQLAlchemy
pip install psycopg
pip install Flask-Migrate
```
## Create user and database in PostgreSQL
```
sudo su - postgres
```
```commandline
psql
```
```commandline
CREATE ROLE hola WITH LOGIN NOSUPERUSER CREATEDB NOCREATEROLE INHERIT NOREPLICATION CONNECTION LIMIT -1 PASSWORD 'h';
```
* Show **pg_hba.conf** path
```commandline
show hba_file;
```
and Ctrl+D to exit psql and postgres user session
* Update pg_hba.conf

Search line
```
local   all             postgres                                peer
```
Add in the next line
```
local   all             hola                                  trust
```
Restart postgresql service
```
sudo systemctl restart postgresql
```
* Test new hola user
```commandline
psql -d postgres -U hola -W
```
* Create database
```
create database hola;
```
### For access to database from remote host 
* Edit **postgresql.conf** file in the same directory of **pg_hba.conf** file
* Enable or add: listen_addresses = 'ip server'
* In **pg_hba.conf** add the next line:
```
host    all             hola          remote.host.ip/24.mask.number         trust
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
## Migrations
```
flask --app flaskr db init
flask --app flaskr db migrate
flask --app flaskr db upgrade
```

## Run
```
flask --app flaskr run --debug
```
