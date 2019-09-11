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
    if request.method == "POST":
        month = request.calculations["month"]
        year = request.calculations["year"]
        value = request.calculations["fundvalue"]
        fprofile = None
        intclass = request.calculations["interestClass"]
        interest = request.calculations["interest"]
        donation = request.calculations["donation"]
        spending = request.calculations["spending"]
        recap = request.calculations["recap"]
        distribution = request.calculations["distribution"]
        timeframe = request.calculations["timeframe"]
        addContribution = request.calculations['additionalContribution']

        if(intclass == "E"):
            calc = classEFG(month,year,value,fprofile,intclass,interest,donation,recap,distribution,timeframe)
        elif(intclass == "F"):
            calc = classEFG(month,year,value,fprofile,intclass,interest,donation,recap,distribution,timeframe)
        elif(intclass == "G"):
            calc = classEFG(month,year,value,fprofile,intclass,interest,donation,recap,distribution,timeframe)
        elif(intclass == "H"):
            calc = classH(month,year,value,fprofile,intclass,interest,spending,addContribution,timeframe)
        elif(intclass == "A"):
            calc = classA(month,year,value,fprofile,intclass,interest,spending,recap,distribution,timeframe)
        elif(intclass == "N"):
            calc = classN(month,year,value,fprofile,intclass,interest,spending,addContribution,timeframe)
        elif(intclass == "Q"):
            calc = classQ(month,year,value,fprofile,intclass,interest,spending,addContribution,timeframe)
        elif(intclass == "S"):
            calc = classS(month,year,value,fprofile,intclass,interest,spending,addContribution,timeframe)

        return render_template("calcs.html", title='Calculation Page', calc=calc)
    return render_template("calcs.html", title='Calculation Page')

@app.route('/profile')
def profile():
    return render_template("profile.html", title='Profile')
