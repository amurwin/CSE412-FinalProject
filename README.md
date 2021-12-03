# CSE412-FinalProject
This application was developed and tested on ```Ubuntu-LTS 18.04```
# Install & Setup Postgres
*  **Note:** If you already have postgres installed and setup you might need to run ```sudo service postgresql start``` to get postgres up and running when you turn on your computer
* Download postgres with: ```sudo apt install postgresql```
* Login to your user (postgres here) and set the password
  * ```sudo -u postgres psql -c "ALTER USER postgres PASSWORD '<password>';"```
* Login to the postgres shell:
  * ```sudo -u postgres psql```
* Once you are in postgres run the following command to make a new database:
  * ```CREATE DATABASE <database name>;```
* Exit postgres with ```\q``` and back in the main terminal load in the SQL dump
  * ```sudo -u postgres psql <database name> < /path/to/pokemondb.sql```

# Setup Python
* Install python 3
* Install Django: ```pip install Django```
* Install psycopg2: ```pip install psycopg2-binary```

# Setting Up Django
* In ```pokemonMain/pokemonMain/settings.py``` the DATABASES needs to be changed to the postgre database set up previously
* Look at lines 77-86
* Arguments:
  * ENGINE: what SQL backend to use
  * NAME: Name of database being used
  * USER: Username used to login to postgres
  * PASSWORD: Password of your postgres user
  * HOST: Where you database is located, if local use ```127.0.0.1```
  * PORT: Port where database is stored. Default is ```5432```

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pokemondb', 
        'USER': 'postgres', 
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}
```
* Run migrations for Django (Make sure you are in ```/pokemonMain```:
  * ```python manage.py makemigrations```
  * ```python manage.py migrate```

# Run The Site
* Finally you can start the server and load the site!
  * ```python manage.py runserver```
