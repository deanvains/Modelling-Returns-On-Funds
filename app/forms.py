from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, IntegerField, 
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

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
    spending = StringField('spending')
    recap = StringField('recap')
    distribution = DecimalField('distribution')
    additionalContribution = StringField('additionalContribution')
    timeframe = IntegerField('timeframe')
    submit = SubmitField('Sign In')

