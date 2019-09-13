from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User#, expected, actual
from app.forms import calculationForm, LoginForm, RegistrationForm
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
        donation = 0 #form.donation.data
        spending = 0 #form.spending.data
        recap = 0 #form.recap.data
        distribution = form.distribution.data
        timeframe = form.timeframe.data
        addContribution = 0 #form.additionalContribution.data

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
        user = User(username=form.username.data, email=form.email.data)
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