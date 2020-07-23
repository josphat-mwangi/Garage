from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader

def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__= 'users'

    
    #Columns
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    comments = db.relationship('Comment', backref='user', lazy="dynamic")

    @property

    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash= generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    
    def __repr__(self):
        return f'User{self.username}'


class Comment(db.Model):
    __tablename__= 'comment'

    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.String(2000))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    timestamp = db.column(db.DateTime())
    path = db.Column(db.Text, index=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls):
        comments = Comment.query.filter_by().all()
        return comments

   