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

run a container (based on a prebuilt image) in the named pod

	podman run --name NAME-OF-CONTAINER -env-file .env


## part 4: Django, PostgreSQL & Podman

_https://www.richardwalker.dev/podman-postgres.html_


## Extra Notes

can load env variables from file by changing python code from `'NAME': os.environ['DATABASE_NAME']`  to `'NAME': os.environ.get("DATABASE_NAME")`
save the variables to a .env file and load it in the run command with the flag -env-file=.env


non-symmetrical port mapping needs to be defined when creating the pod

	$:~/projects/ngin$ podman pod create -p 8888:80 -n ngin-pod
	daa6e8ad645c09c997b50902140a5e4aa6ed79a3407eaff240b85d0f3caa3d7d

	$:~/projects/ngin$ podman run --pod ngin-pod -p 8888:80 --name ngin-ctr -d nginx
	8922ec5974eea7fe2c71df9e4e1590078c85091ada3a4ff68b508dd2c6931437

	$:~/projects/ngin$ curl localhost:8888
	podman rulez


start another container in the same pod (not shown is: apt-get update; apt-get install curl)

	$ podman run --pod ngin-pod --name shell-ctr -it ubuntu sh
	# curl localhost:80
	podman rulez