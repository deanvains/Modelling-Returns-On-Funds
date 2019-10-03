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
    month = StringField('Month')
    year = IntegerField('Year')
    fundvalue = IntegerField('Fund Value')
    interestClass = StringField('Interest Class')
    donation = StringField('Donation Amounts')
    spending = StringField('Spending Amounts') 
    recap = StringField('Recapitalization Amounts') 
    distribution = DecimalField('Distribution Rate') 
    operatingDistribution = StringField('Operating Capital Distribution') 
    additionalContribution = StringField('Additional Contribution') 
    timeframe = IntegerField('Time Frame')
    savedata = BooleanField('Click the box to save your result.')
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
			

class ResetPassword(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	currentPassword = PasswordField('Current Password', validators=[DataRequired()])
	newPassword = PasswordField('New Password', validators=[DataRequired()])
	newPassword2 = PasswordField('Repeat New Password', validators=[DataRequired(), EqualTo('newPassword')])
	submit = SubmitField('Reset Password')
	
	
class ForgottenPassword(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	newPassword = PasswordField('New Password', validators=[DataRequired()])
	newPassword2 = PasswordField('Repeat New Password', validators=[DataRequired(), EqualTo('newPassword')])
	submit = SubmitField('Reset Password')
            
            
class InterestRatesForm(FlaskForm):
    ClassE = StringField('Long Term Pool - Class E')
    ClassF = StringField('Long Term Pool - Class F')
    ClassG = StringField('Long Term Pool - Class G')
    ClassH = StringField('Medium Term Pool - Class H')
    ClassA = StringField('Short Term Pool - Class A')
    ClassN = StringField('Short Term Pool - Class N')
    ClassQ = StringField('Short Term Pool - Class Q')
    ClassS = StringField('Cash Pool - Class S')
    submit = SubmitField('Submit')
    
class RemovalForm(FlaskForm):
    rid = IntegerField('Which item would you like to remove?')
    submit = SubmitField('Submit')

class makeAdmin(FlaskForm):
    adminid = IntegerField('Please enter user ID to make admin.')
    submit = SubmitField('Submit')

class storedSelect(FlaskForm):
    storedid = IntegerField('Which result would you like to view?')
    submit = SubmitField('Submit')

class compForm(FlaskForm):
    stored1 = IntegerField('Which is the first result you would to view?')
    stored2 = IntegerField('Which is the first result you would to view?')
    submit = SubmitField('Submit')