from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<id {}, User {}>'.format(self.id, self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def is_committed(self):
        return self.id is not None
    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    
""""
class expected():
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    month = db.Column(db.String(64))
    year = db.Column(db.Integer)
    value = db.Column(db.Integer)
    fprofile = db.Column(db.Integer)
    intclass = db.Column(db.String(64))
    interest = db.Column(db.Integer) #not an integer
    #donation = db.Column(db.Integer)
    #spending = db.Column(db.Integer)
    recap = db.Column(db.Integer)
    distribution = db.Column(db.Integer) #not an integer
    timeframe = db.Column(db.Integer)
    #addContribution = db.Column(db.Integer)


class actual():
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(140))
"""
