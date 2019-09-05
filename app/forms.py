from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


#class calculations(FlaskForm):
#    interestClass = 
#    openingBalance =
#    StartMonth = 
#    endMonth =
#    interestRate = 
#    SpendingProfile = 
#    ProfileOfFundsReceipt = 
#    ChangeInSpending =
#    AdditionalDonations = 
#    recapitalisation = 
#    capitalDistribution = 
#    customDistribution = 

#    if(interestClass == classE):
#        return
#    elif(interestClass == classF):
#        return
#    elif(interestClass == classG):
#        return
#    elif(interestClass == classH):
#        return
#   elif(interestClass == classA):
#       return
#    elif(interestClass == classN):
#        return
#    elif(interestClass == classQ):
#        return
#    elif(interestClass == classS):
#        return