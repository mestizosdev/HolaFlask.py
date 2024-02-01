# Database

## Create user and database in PostgreSQL
```
sudo su - postgres
```
```
psql
```
```
CREATE ROLE hola WITH LOGIN NOSUPERUSER CREATEDB NOCREATEROLE INHERIT NOREPLICATION CONNECTION LIMIT -1 PASSWORD 'h';
```
* Show **pg_hba.conf** path
```
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
```
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