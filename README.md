[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/worked-django-examples/tables2_base)

# Styling for django-tables2

from https://github.com/worked-django-examples 

## Purpose

This repo has examples of styling with bootstrap4 for tables2

### repo setup 

 - make sure you have `pip install django-bootstrap4` or equivalent
 - add `bootstrap4` to `installed apps`
 - in `settings.py`, anywhere in the file, assign the default template:  `DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap.html"`


## to populate data on your local, using docker

`docker run --name postgresql -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 --restart always -v /tmp/pgdata:/tmp/var/lib/postgresql/data -d postgres:13`

run the worldbank-population.py script in the etl directory
