flitterFlask
============

clone of twitter created using flask framework for python 

Project Requirements:

1. Users need to be able to register with Flitter using standard username and password credentials. There is no need to address forgotten passwords.
2. Passwords should be hashed in the database. Use a message digest and salt to obscure the passwords.
3. Authenticated users should see a list of their latest posts sorted by date upon login.
4. There should be a "create new post" input field above the list of previous posts.
5. Posts are limited to 200 characters or less. Handle this with client­side validation.
6. All posts are public and should be accessible by this URL convention:
http://localhost:port/flitter/user/username

Optional enhancements
1. Implement pagination to limit posts to 10 per page

Sources:

Flask Mega tutorial: http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
for password hashing: http://flask.pocoo.org/snippets/54/
for login management: https://flask-login.readthedocs.org/en/latest/


Some Open Issues and possible Additions:
1. Currently, no facebook login feature is included.
2. Would like to limit posts to 200 characters by implementing a visual cue that shows how far beyond 200 chars user has gone(similar to twitter).
3. Add feature for deleting and editing posts.

first things first, get pip if you dont already have it and install these dependencies:
flask/bin/pip install flask==0.9
flask/bin/pip install flask-login
flask/bin/pip install flask-openid
flask/bin/pip install flask-mail==0.7.6
flask/bin/pip install sqlalchemy==0.7.9
flask/bin/pip install flask-sqlalchemy==0.16
flask/bin/pip install sqlalchemy-migrate==0.7.2
flask/bin/pip install flask-whooshalchemy==0.55a
flask/bin/pip install flask-wtf==0.8.4

then clone the repo, and use python to run the db_create.py and then db_migrate.py files.
Next, execute python run.py and navigate to http://localhost:5000 and register some users, login and begin posting to test the app.



