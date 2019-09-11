from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, IntegerField, MultipleFileField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class calculations(FlaskForm):
    month = StringField('month')
    year = IntegerField('year')
    fundvalue = IntegerField('fundvalue')
    #fProfile = none
    interestClass = StringField('interestClass')
    interest = DecimalField('interest')
    donation = MultipleFileField('donation')
    spending = MultipleFileField('spending')
    recap = MultipleFileField('recap')
    distribution = DecimalField('distribution')
    timeframe = IntegerField('timeframe')
    submit = SubmitField('Sign In')

