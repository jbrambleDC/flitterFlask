from flask import Flask
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir
from flask.ext.sqlalchemy import SQLAlchemy

#config flask
app = Flask(__name__)
app.config.from_object('config')

#connect to database
db = SQLAlchemy(app)
dbsess = db.session

#login management set up
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
#oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models
