from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from werkzeug.urls import url_parse
from calculations.ClassHS import classH, classS
from calculations.ClassN import classN
from calculations.ClassQ import classQ
from calculations.ClassEFG import classEFG
from calculations.ClassA import classA

@app.route('/')
@app.route('/homepage')
def homepage():

    return render_template("homepage.html", title='Home Page')

@app.route('/calc',methods=["GET", "POST"])
def calcs():
#    if request.method == "POST":
#        #might need to check form name match
#        interestClass = request.calculations["interestClass"]
#        openingBalance = request.calculations["openingBalance"]
#        StartMonth = request.calculations["StartMonth"]
#        endMonth = request.calculations["endMonth"]
#        interestRate = request.calculations["interestRate"]
#        SpendingProfile = request.calculations["SpendingProfile"]
#        ProfileOfFundsReceipt = request.calculations["ProfileOfFundReceipts"]
#        ChangeInSpending = request.calculations["ChangeInSpending"]
#        AdditionalDonations = request.calculations["AdditionalDonations"]
#        recapitalisation = request.calculations["recapitalisation"]
#        capitalDistribution = request.calculations["capitalDistribution"]
#        customDistribution = request.calculations["customDistribution"]

#    calc = null
    #need to put parameters in
#    if(interestClass == classE):
#        calc = ClassEFG()
#    elif(interestClass == classF):
#        calc = ClassEFG()
#    elif(interestClass == classG):
#        calc = ClassEFG()
#    elif(interestClass == classH):
#       calc = ClassHS()
#    elif(interestClass == classA):
#        calc = ClassA()
#    elif(interestClass == classN):
#        calc = ClassN()
#   elif(interestClass == classQ):
#        calc = ClassQ()
#    elif(interestClass == classS):
#        calc = ClassHS()



    return render_template("calcs.html", title='Calculation Page')
    #return render_template("calcs.html", title='Calculation Page', calc=calc)

@app.route('/profile')
def profile():
    return render_template("profile.html", title='Profile')
