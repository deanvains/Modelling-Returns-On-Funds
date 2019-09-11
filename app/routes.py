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
#        calc = ClassEFG(month,year,value,fprofile,intclass,interest,donation,recap,distribution,timeframe)
#    elif(interestClass == classF):
#        calc = ClassEFG(month,year,value,fprofile,intclass,interest,donation,recap,distribution,timeframe)
#    elif(interestClass == classG):
#        calc = ClassEFG(month,year,value,fprofile,intclass,interest,donation,recap,distribution,timeframe)
#    elif(interestClass == classH):
#       calc = ClassH(month,year,value,fprofile,intclass,interest,spending,addContribution,timeframe)
#    elif(interestClass == classA):
#        calc = ClassA(month,year,value,fprofile,intclass,interest,spending,recap,distribution,timeframe)
#    elif(interestClass == classN):
#        calc = ClassN(month,year,value,fprofile,intclass,interest,spending,addContribution,timeframe)
#   elif(interestClass == classQ):
#        calc = ClassQ(month,year,value,fprofile,intclass,interest,spending,addContribution,timeframe)
#    elif(interestClass == classS):
#        calc = ClassS(month,year,value,fprofile,intclass,interest,spending,addContribution,timeframe)



    return render_template("calcs.html", title='Calculation Page')
    #return render_template("calcs.html", title='Calculation Page', calc=calc)

@app.route('/profile')
def profile():
    return render_template("profile.html", title='Profile')
