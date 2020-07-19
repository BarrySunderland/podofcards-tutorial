# podofcards-tutorial

this tutorial follows along Richard Walker's tutorial series on using podman with Django, Django REST Framework and postgreSQL.

## part 1: Django REST framework

_https://www.richardwalker.dev/django-rest.html_

## part 2: Django

_https://www.richardwalker.dev/django-dev.html_

## part 3: Working with Podman

_https://www.richardwalker.dev/django-podman.html_


create a pod named cardpod with ports 8000, 7000 & 5432 mapped to the host machine

	podman pod create -p 8000 -p 7000 -p 5432 -n cardpod



## part 4: Django, PostgreSQL & Podman

_https://www.richardwalker.dev/podman-postgres.html_
