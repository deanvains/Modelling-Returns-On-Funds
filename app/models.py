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
    

class expected():
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


    month = StringField('month')
    year = IntegerField('year')
    fundvalue = IntegerField('fundvalue')
    #fProfile = none
    interestClass = StringField('interestClass')
 
    donation = StringField('donation') #multiple file field could be incorrect could also use FieldList
    spending = StringField('spending') #multiple file field could be incorrect could also use FieldList
    recap = StringField('recap') #multiple file field could be incorrect could also use FieldList
    distribution = DecimalField('distribution') #multiple file field could be incorrect could also use FieldList
    additionalContribution = StringField('additionalContribution') #multiple file field could be incorrect could also use FieldList
    timeframe = IntegerField('timeframe')
    submit = SubmitField('Calculate')

