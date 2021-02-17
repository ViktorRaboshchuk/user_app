In this article we will see how to deploy a Flask app on Linux using Docker.

## Step #1 - Create ETL procedure 

In this project we will work with data from https://randomuser.me/ - it’s free and easy to use open-source API for generating random users data. 

I decided to use Postgres DB for this project because Postgres is one of the most widely used Docker images that run in containers and it’s simple to use. But of course somebody could use SQLite3 for this small project.

Let’s see the structure of our project. 

So in the generate_users.py script we will have:
Method for creating DB table
Method for inserting fetched data from API
Method for fetching data from API

Here we call the API with specific parameters like gender, nationality and number of result users, and then parsing the response result.

## Step #2 - Create Flask app

In the app.py script that contains our Flask functions we have only 2 methods, for each URL that user triggers. 

Our first method simply getting data from DB, and rendering it in our HTML file where we will see list of all 100 user

Our second method also renders data from the database, but to the users template where we can see more information about randomly generated users.
 
And if you don’t like him, you can delete him. Deleting process occurs through POST requests that our Python method receives.

And also we can see randomly generated user locations on map made with Folium package.

## Step #3 - Create Docker and docker-compose files
Docker is a platform that facilitates the process of building, launching and distributing applications, where each application runs in separate units called containers. And we will use Docker Compose technology that will allow us to deploy our app, combining separate containers. 

So our docker-compose file will launch 3 separate services that are placed in separate folders with unique Dockerfiles, and those Dockerfiles will create a working directories, copy all needed files, and run installations of all needed packages. Each Dockerfile has a CMD command that will be executed when the docker-compose file will start the containers.
Using depends_on we tell docker-compose file to wait for DB to be created, and only then it will start filling the DB table and run Flask applications.

By the way, Docker will use db from docker-compose file  as a hostname of our DB.


In order to be able to see current application from my local machine  I specified port as ‘0.0.0.0’ in Flask file, but if you will have any troubles with that, try to do following steps:
Go to VM Manager
Open Settings of our VM
Go to Network -> Advanced -> Port Formatting
Add Name of your app, and IP = ‘0.0.0.0’, Port = 5000
If, on your local machine, address ‘0.0.0.0:5000’ won’t work try ‘127.1.0.0:5000’

# Step #4 - Run application

Download Git repository
git clone https://github.com/ViktorRaboshchuk/user_app.git

Changing directory
cd user_app

Build and Run app
docker-compose up --build

To shut down running app use
docker-compose down


