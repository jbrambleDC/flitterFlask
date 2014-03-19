from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, dbsess, lm,models
from forms import RegisterForm, LoginForm, CreatePostForm
from models import User,Post
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from config import POSTS_PER_PAGE

#from https://flask-login.readthedocs.org/en/latest/
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
@app.route('/index/<int:page>', methods = ['GET', 'POST']) #implements pagination
def index(page = 1):
	user = g.user
	if user.is_authenticated():
		posts = Post.query.filter_by(userid=user.id).order_by("timestamp desc").paginate(page, POSTS_PER_PAGE, False)
		return render_template("yourposts.html",
			user = user,
			title = user.username,
			posts = posts)
	else:
		return render_template("index.html",
			loginform = LoginForm(),
			registerform = RegisterForm())
	

#password hashing/salt http://flask.pocoo.org/snippets/54/
@app.route('/login', methods = ['GET', 'POST'])
@app.route('/login/<int:page>', methods = ['GET', 'POST']) #pagination
def login(page = 1):
    form = LoginForm()
    user = g.user
    if user is not None and user.is_authenticated():
        return redirect(url_for('index'))
    if form.validate_on_submit():
    	#checks if form is left empty
    	if form.username.data == None or form.password.data == None:
    		return redirect(url_for('index'))
    	#allows user to login with email
    	if form.username.data.find('@') != -1:
    		username = form.username.data.split('@')[0]
    	else:
    		username = form.username.data
    	user = models.User.query.filter_by(username=username).first()
    	#if username cannot be found
    	if user == None:
			flash('User not found.')
			return redirect(url_for('index'))
		#checks if passwords match
    	if check_password_hash(user.password,form.password.data):
    		login_user(user)
    if form.password.data and form.username.data and check_password_hash(user.password,form.password.data):		
    	return render_template('yourposts.html', 
    		title = user.username,
    		user = user,
    		posts = user.posts.order_by("timestamp desc").paginate(page, POSTS_PER_PAGE, False),
			)
    else:
    	flash('Incorrect password')
    	return render_template('index.html',
    		loginform = form,
    		registerform = RegisterForm()
    		)


@app.route('/register', methods = ['GET','POST'])
def register():
	form = RegisterForm()
	if form.validate():
		#if user registers with email, create a username, from their email
		if form.newusername.data.find('@') != -1:
			username = form.newusername.data.split('@')[0]
			email = form.newusername.data
		else:
			username = form.newusername.data
			email = None
		#checks if username already exists
		checkuser = User.query.filter_by(username = username).first()
		if checkuser != None:
			flash('user name already taken')
			return redirect(url_for('index'))
		else:
			#add new user to database
			newuser = models.User(username=username, email = email, password=generate_password_hash(form.password.data), fullname = form.fullname.data)
			dbsess.add(newuser)
			dbsess.commit()
			login_user(newuser)
		#ins = User.insert().values(username=form.username.data, password=generate_password_hash(form.password.data), fullname=form.fullname.data)
		#db.session.execute(ins)
		#db.session.commit()
		return redirect(url_for('index'))
	return render_template('index.html',
		registerform = form,
		loginform = LoginForm())

@app.route('/newpost', methods=['GET','POST'])
@login_required
def createpost():
	form = CreatePostForm(request.form)
	if form.validate_on_submit():
		newpost = Post(posttext = form.posttext.data, timestamp = datetime.datetime.now(), author = g.user)
		dbsess.add(newpost)
		dbsess.commit()
    	return redirect(url_for('index'))
	return render_template('index.html',form = form)

@app.route('/post', methods =['GET','POST'])
@login_required
#renders form for new post
def newpost():
	form = CreatePostForm()
	return render_template('post.html',form=form)

@app.route('/flitter/user/<username>')
@app.route('/flitter/user/<username>/<int:page>', methods = ['GET', 'POST']) #pagination
def user(username, page = 1):
    user = User.query.filter_by(username = username).first()
    #check if invalid user is entered
    if user == None:
        flash('User not found.')
        return redirect(url_for('index'))
    posts = user.posts.order_by("timestamp desc").paginate(page, POSTS_PER_PAGE, False)
    return render_template('user.html',
        user = user,
        posts = posts)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
