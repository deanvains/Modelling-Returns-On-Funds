from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import calculationForm
from app import app, db
from werkzeug.urls import url_parse
from calculations.ClassH import classH
from calculations.ClassN import classN
from calculations.ClassQ import classQ
from calculations.ClassE import classE
from calculations.ClassA import classA
from calculations.ClassF import classF
from calculations.ClassG import classG
from calculations.ClassS import classS

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template("homepage.html", title='Home Page')

@app.route('/calc',methods=["GET", "POST"])
def calcs():
    form = calculationForm()
    if form.validate_on_submit():
        month = form.month.data
        year = form.year.data
        value =  form.fundvalue.data
        fprofile = None
        intclass = form.interestClass.data
        interest = form.interest.data
        donation = 0 #request.calculations["donation"]
        spending = 0 #request.calculations["spending"]
        recap = 0 #request.calculations["recap"]
        distribution = form.distribution.data
        timeframe = form.timeframe.data
        addContribution = 0 #request.calculations['additionalContribution']

        if(intclass == "E"):
            calc = classE(month,year,value,fprofile,intclass,interest,donation,recap,distribution,timeframe)
        elif(intclass == "F"):
            calc = classF(month,year,value,fprofile,intclass,interest,donation,recap,distribution,timeframe)
        elif(intclass == "G"):
            calc = classG(month,year,value,fprofile,intclass,interest,donation,recap,distribution,timeframe)
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

        return render_template("calcs.html", title='Calculation Page', form=form,calc=calc)
    return render_template("calcs.html", title='Calculation Page', form=form)

@app.route('/profile')
def profile():
    return render_template("profile.html", title='Profile')
