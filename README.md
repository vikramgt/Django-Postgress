# Django-Postgress
CRUD Operations using Django Web Framework and storing it a Postgres Database using Docker and Containers.
I've used a Docker.file which has all the required images and a requirement.txt file which has additional requirements and linked it inside the Docker.file.
I also have a Docker-compose file which has definition of Web service and Postgres. 

Download the files, put it into a directory.
In the terminal go inside the directory and run the command 

sudo docker build 

It will build the images. T
Then use the command

sudo docker-compose up

which will bring up the containers of Web service and Postgres.

Go to localhost:8000 
Add new records and but it will throw an error as we don't have a database yet.
So , open another window of terminal, type in

sudo docker ps

which will bring up all the running containers. Copy the ID of Web container. Then type in 

sudo exec -it <container id> sh

It will go inside the web container. Type in

psqll -U postgres -h database -d postgres

enter password postgres

create a database using 

CREATE DATABASE data;

Keep the name as it is because it is defined as it is in the settings.py file of Django.

The use the database using \c data;

Then on the web page, insert new records. Now it will work correctly
