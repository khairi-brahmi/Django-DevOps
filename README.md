# Django-DevOps

Developer : Khairi Brahmi
***
Phone : +21622449506
==========


Getting Up and Running Locally With Docker
==========================================
 
The steps below will get you up and running with a local development environment.
All of these commands assume you are in the root of your project.


Prerequisites
-------------

* Docker 
* Docker Compose 
 
 
Build the Stack
---------------

This can take a while, especially the first time you run this particular command on your development system::

    $ docker-compose -f docker-compose.yml build 
    
 
Run commands
-------------


As with any shell command that we wish to run in our container, this is done using the ``docker-compose -f docker-compose.yml run --rm`` command:

    $ docker-compose -f docker-compose.yml run --rm web-django python manage.py migrate
    $ docker-compose -f docker-compose.yml run --rm web-django python manage.py createsuperuser
    $ docker-compose -f docker-compose.yml run --rm web-django python manage.py makemigrations

Here, ``web-django`` is the target service we are executing the commands against.

 


Removing All Unused Objects
-------------
    $ docker stop $(docker ps -a -q)
    $ docker rm $(docker ps -a -q)
    $ docker system prune
    $ docker system prune --volumes
    

