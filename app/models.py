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


class InterestRates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ClassE = db.Column(db.Float)
    ClassF = db.Column(db.Float)
    ClassG = db.Column(db.Float)
    ClassH = db.Column(db.Float)
    ClassA = db.Column(db.Float)
    ClassN = db.Column(db.Float)
    ClassQ = db.Column(db.Float)
    ClassS = db.Column(db.Float)

    def __repr__(self):
        return '<id {}, classE {}, classF {},classG {},classH {},class A{}, classN {}, classQ {}, classS {}>'.format(self.id, self.ClassE, self.ClassF, self.ClassG, self.ClassH, self.ClassA, self.ClassN, self.ClassQ, self.ClassS)
    

class expected(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    month = db.Column(db.String(1024))
    year = db.Column(db.Integer)
    value = db.Column(db.Integer)
    intclass = db.Column(db.String(1024))
    donation = db.Column(db.String(1024))
    spending = db.Column(db.String(1024))
    recap = db.Column(db.String(1024))
    distribution = db.Column(db.String(1024))
    timeframe = db.Column(db.Integer)
    addContribution = db.Column(db.String(1024))

    def __repr__(self):
        return '<id {}, User_id {}, month {}, year {} >'.format(self.id, self.user_id, self.month, self.year)