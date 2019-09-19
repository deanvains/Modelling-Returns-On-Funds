from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User, InterestRates

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class calculationForm(FlaskForm):
    month = StringField('month')
    year = IntegerField('year')
    fundvalue = IntegerField('fundvalue')
    #fProfile = none
    interestClass = StringField('interestClass')
    interest = DecimalField('interest')
    donation = StringField('donation') #multiple file field could be incorrect could also use FieldList
    spending = StringField('spending') #multiple file field could be incorrect could also use FieldList
    recap = StringField('recap') #multiple file field could be incorrect could also use FieldList
    distribution = DecimalField('distribution') #multiple file field could be incorrect could also use FieldList
    additionalContribution = StringField('additionalContribution') #multiple file field could be incorrect could also use FieldList
    timeframe = IntegerField('timeframe')
    submit = SubmitField('Calculate')
    
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
            
            
class InterestRates(FlaskForm):
    ClassE = DecimalField('Long Term Pool - Class E')
    ClassF = DecimalField('Long Term Pool - Class F')
    ClassG = DecimalField('Long Term Pool - Class G')
    ClassH = DecimalField('Medium Term Pool - Class H')
    ClassA = DecimalField('Short Term Pool - Class A')
    ClassN = DecimalField('Short Term Pool - Class N')
    ClassQ = DecimalField('Short Term Pool - Class Q')
    ClassS = DecimalField('Cash Pool - Class S')
    submit = SubmitField('Submit')