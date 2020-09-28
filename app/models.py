from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime


# ...
@login_manager.user_loader
def load_user(id):
        return User.query.get(int(id))
       

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(100000))
    profile_pic_path = db.Column(db.String(255))
    pass_secure = db.Column(db.String(1000000))

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    
    def __repr__(self):
        return f'User {self.username}'
class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    category= db.Column(db.String(),index = True)
    content= db.Column(db.String()) 
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship('Comment', backref = 'blog1', lazy = 'dynamic')

    def __repr__(self):
        return f'blog1 {self.content}'          

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    blog_id = db.Column(db.Integer,db.ForeignKey ('blog.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    content= db.Column(db.String(1000000)) 

    def __repr__(self):
        return f'Comment :content {self.content}' 
class Subscriber(UserMixin, db.Model):
    __tablename__="subscribers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    title = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)


    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_subscribers(cls,id):
        return Subscriber.query.all()
         

    def __repr__(self):
        return f'User {self.email}'        
       


        