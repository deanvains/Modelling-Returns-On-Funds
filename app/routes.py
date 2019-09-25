from flask import render_template, flash, redirect, url_for, request, make_response
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, InterestRates, expected
from app.forms import calculationForm, LoginForm, RegistrationForm, InterestRates
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
from calculations.findDec import findDec
from calculations.calDynamic import calcDyn
from calculations.calcMonth import calcMonths
from calculations.test import testdata
from app.exports import pdfGen
import traceback

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template("homepage.html", title='Home Page')

@app.route('/calc',methods=["GET", "POST"])
def calcs():
    
    if request.method == 'POST':
        if 'submit' in request.values:
            form = calculationForm()
            if form.validate_on_submit():
                try:
                    month = form.month.data
                    year = form.year.data
                    value =  form.fundvalue.data
                    fprofile = None
                    intclass = form.interestClass.data
                    interest = InterestRates.query.first()
                    distribution = form.distribution.data
                    timeframe = form.timeframe.data
                    if form.donation.data == '' or form.donation.data == '0':
                        donation = {}
                    else:
                        donation = calcDyn(form.donation.data,month,year,timeframe)
                    #spending = form.additionalContribution.data
                    if form.spending.data == '' or form.spending.data == '0' :
                        spending = {}
                    else:
                        spending = calcDyn(form.spending.data,month,year,timeframe)
                    if form.recap.data == '' or form.recap.data == '0':
                        recap = {}
                    else:
                        recap = calcDyn(form.recap.data,month,year,timeframe)
                    if form.operatingDistribution.data == '' or form.operatingDistribution.data == '0' :
                        operatingDistribution = {}
                    else:
                        operatingDistribution = calcDyn(form.operatingDistribution.data,month,year,timeframe)
                    if form.additionalContribution.data == '' or form.additionalContribution.data == '0':
                        addContribution = {}
                    else:
                        addContribution = calcDyn(form.additionalContribution.data,month,year,timeframe)
                    decMonth = findDec(month)
                    savedata = form.savedata.data

                    if(savedata == True and current_user.is_authenticated):
                        clientsave = expected(user_id=current_user.id,month=month,year=year,value=value,intclass=intclass,donation=donation,
                        spending=spending,recap=recap,distribution=distribution,timeframe=timeframe,addContribution=addContribution)
                        db.session.add(clientsave)
                        db.session.commit()

                    if intclass == "E":
                        thisinterest = interest.classE
                        calc = classE(month,year,value,fprofile,intclass,thisinterest,donation,recap,distribution,timeframe)
                    elif intclass == "F":
                        thisinterest = interest.classF
                        calc = classF(month,year,value,fprofile,intclass,thisinterest,donation,recap,operatingDistribution,timeframe)
                    elif intclass == "G" :
                        thisinterest = interest.classG
                        calc = classG(month,year,value,fprofile,intclass,thisinterest,donation,recap,operatingDistribution,timeframe)
                    elif(intclass == "H"):
                        thisinterest = interest.classH
                        calc = classH(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
                    elif intclass == "A":
                        thisinterest = interest.classA
                        calc = classA(month,year,value,fprofile,intclass,thisinterest,spending,recap,operatingDistribution,timeframe)
                    elif(intclass == "N"):
                        thisinterest = interest.classN
                        calc = classN(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
                    elif(intclass == "Q"):
                        thisinterest = interest.classQ
                        calc = classQ(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
                    elif(intclass == "S"):
                        thisinterest = interest.classS
                        calc = classS(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)

                    calc = testdata() #testing
                    return render_template("calcs.html", title='Calculation Page', form=form, calc=calc, years=year,timeframe=timeframe,decMonth = decMonth,spending =spending)
                except:
                    traceback.print_exc() #To print error Trace
                    return render_template("calcs.html", title='Calculation Page', form=form,calc = [[0],[0]],timeframe = 0,years=0,decMonth = 0,spending = 0)
        else:
            return pdfGen()

    
    form = calculationForm()
    calc = testdata() #testing

    #calc in the render template has been modified for testing
    return render_template("calcs.html", title='Calculation Page', form=form,calc = calc,timeframe = 0,years=0,decMonth = 0,spending = 0)

#@app.route('/pdfCreator')
#def pdfCreator():
#    return pdfGen()


@app.route('/profile',methods=["GET", "POST"])
def profile():
    return render_template("profile.html", title='Profile', expected=expected.query.all())


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('signin'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('homepage')
        return redirect(next_page)
    return render_template('signin.html', title='Sign In', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        #user.admin = False  # user not admin by default
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('signin'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = InterestRates()
    #intRates = InterestRates.query(InterestRates).order_by(InterestRates.id.desc()).first()
    #if intRates is None:
    #    return redirect(url_for('admin'))
    if form.validate_on_submit():
        interest_rates = InterestRates(ClassE=form.ClassE.data, ClassF=form.ClassF.data, ClassG=form.ClassG.data, ClassH=form.ClassH.data, ClassA=form.ClassA.data, ClassN=form.ClassN.data, ClassQ=form.ClassQ.data, ClassS=form.ClassS.data)
        db.session.add(interest_rates)
        db.session.commit()
        return redirect(url_for('admin'))
    #return render_template('admin.html', title='Admin', form=form, value=intRates)
    return render_template('admin.html', title='Admin', form=form)
