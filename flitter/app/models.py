from app import db

#ROLE_USER = 0
#ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(100))
    fullname = db.Column(db.String(100))
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)
    
    def __repr__(self):
        return '<User %r>' % (self.username)


class Post(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  userid = db.Column(db.Integer, db.ForeignKey('user.id'))
  posttext = db.Column(db.String(300))
  timestamp = db.Column(db.DateTime)
  

  def __repr__(self):
    return '<Post %r>' % (self.posttext)