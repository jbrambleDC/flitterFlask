flitterFlask
============

clone of twitter created using flask framework for python:
http://flitterfavmed.herokuapp.com/

###note on heroku deployment:
The code used to deploy on Heroku is slightly different than the code in this repo, one must change their config file so that SQLALCHEMY_DATABASE_URI points at a postgresql database that has been added to the heroku app. Refer to the Flask Mega Tutorial, as well Source #4 for detailed walkthrough of Heroku Deployment for flask apps. Doing this also requires the Heroku deployment to have a list of dependencies called requirements.txt(that also contains psycopg2, and a Procfile. These files tell Heroku which dependencies to get, and how to create the database and run the app. navigate to http://flitterfavmed.herokuapp.com/flitter/user/jordanbramble to see a sample user with some sample posts that demonstrate pagination

##Project Requirements:

1. Users need to be able to register with Flitter using standard username and password credentials. There is no need to address forgotten passwords.
2. Passwords should be hashed in the database. Use a message digest and salt to obscure the passwords.
3. Authenticated users should see a list of their latest posts sorted by date upon login.
4. There should be a "create new post" input field above the list of previous posts.
5. Posts are limited to 200 characters or less. Handle this with client­side validation.
6. All posts are public and should be accessible by this URL convention:
http://localhost:port/flitter/user/username

##Optional enhancements: 

1. Implement pagination to limit posts to 10 per page
2. Facebook Registration (not included on this iteration)

##Sources:

1. Flask Mega tutorial: http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
2. For password hashing: http://flask.pocoo.org/snippets/54/
3. For login management: https://flask-login.readthedocs.org/en/latest/
4. For configuring postgresql server on Heroku http://beatofthegeek.com/2013/04/how-to-setup-postgresql-python-flask.html


##Some Open Issues and Possible Additions:

1. Currently, no facebook login feature is included.
2. Would like to limit posts to 200 characters by implementing a visual cue that shows how far beyond 200 chars user has gone(similar to twitter).
3. Add feature for deleting and editing posts.
4. add error handling, so that there is a custom page to represent 404,500 error etc.

##Running Flitter Locally

first things first, get pip if you dont already have it and install the dependencies from dependencies.txt:
```
flask/bin/pip install flask==0.9
flask/bin/pip install flask-login
flask/bin/pip install flask-openid
flask/bin/pip install flask-mail==0.7.6
flask/bin/pip install sqlalchemy==0.7.9
flask/bin/pip install flask-sqlalchemy==0.16
flask/bin/pip install sqlalchemy-migrate==0.7.2
flask/bin/pip install flask-whooshalchemy==0.55a
flask/bin/pip install flask-wtf==0.8.4
```

then clone the repo, and use python to run the db_create.py and then db_migrate.py files.
Next, execute python run.py and navigate to http://localhost:5000 and register some users, login and begin posting to test the app.



