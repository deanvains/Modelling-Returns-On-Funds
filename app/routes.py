from flask import render_template, flash, redirect, url_for, request, make_response
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, InterestRates, expected
from app.forms import calculationForm, LoginForm, RegistrationForm, InterestRatesForm, RemovalForm, makeAdmin, ResetPassword, ForgottenPassword, storedSelect
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
                    month = form.month.data.strip()
                    year = form.year.data
                    if len(str(year)) != 4:
                        raise Exception("Invalid Years")
                    value =  form.fundvalue.data
                    fprofile = None
                    intclass = form.interestClass.data.strip()
                    interest = InterestRates.query.first()
                    distribution = form.distribution.data
                    timeframe = form.timeframe.data
                    
                    if form.donation.data == '' or form.donation.data == '0':
                        donation = {}
                    else:
                        dynVal = form.donation.data.split(',')
                        yearValue = 0
                        for group in dynVal:
                            grpLst = group.split("-")
                            monthVal = grpLst[0].strip().lower()
                            yearVal = grpLst[1].strip()
                            if yearVal.isdigit() == True :
                                if int(yearVal) < int(yearValue) :
                                    raise Exception("Year 2 is lower than year 1")
                                else:
                                    yearValue = yearVal
                        donation = calcDyn(form.donation.data,month,year,timeframe)
                    #spending = form.additionalContribution.data
                    if form.spending.data == '' or form.spending.data == '0' :
                        spending = {}
                    else:
                        dynVal = form.spending.data.split(',')
                        yearValue = 0
                        for group in dynVal:
                            grpLst = group.split("-")
                            monthVal = grpLst[0].strip().lower()
                            yearVal = grpLst[1].strip()
                            if yearVal.isdigit() == True :
                                if int(yearVal) < int(yearValue) :
                                    raise Exception("Year 2 is lower than year 1")
                                else:
                                    yearValue = yearVal
                        spending = calcDyn(form.spending.data,month,year,timeframe)
                    if form.recap.data == '' or form.recap.data == '0':
                        recap = {}
                    else:
                        dynVal = form.recap.data.split(',')
                        yearValue = 0
                        for group in dynVal:
                            grpLst = group.split("-")
                            monthVal = grpLst[0].strip().lower()
                            yearVal = grpLst[1].strip()
                            if yearVal.isdigit() == True :
                                if int(yearVal) < int(yearValue) :
                                    raise Exception("Year 2 is lower than year 1")
                                else:
                                    yearValue = yearVal
                        recap = calcDyn(form.recap.data,month,year,timeframe)
                    if form.operatingDistribution.data == '' or form.operatingDistribution.data == '0' :
                        operatingDistribution = {}
                    else:
                        dynVal = form.operatingDistribution.data.split(',')
                        yearValue = 0
                        for group in dynVal:
                            grpLst = group.split("-")
                            monthVal = grpLst[0].strip().lower()
                            yearVal = grpLst[1].strip()
                          
                            if yearVal.isdigit() == True :
                                if int(yearVal) < int(yearValue) :
                                    raise Exception("Year 2 is lower than year 1")
                                else:
                                    yearValue = yearVal
                        operatingDistribution = calcDyn(form.operatingDistribution.data,month,year,timeframe)
                    if form.additionalContribution.data == '' or form.additionalContribution.data == '0':
                        addContribution = {}
                    else:
                        dynVal = form.additionalContribution.data.split(',')
                        yearValue = 0
                        for group in dynVal:
                            grpLst = group.split("-")
                            monthVal = grpLst[0].strip().lower()
                            yearVal = grpLst[1].strip()
                            if yearVal.isdigit() == True :
                                if int(yearVal) < int(yearValue) :
                                    raise Exception("Year 2 is lower than year 1")
                                else:
                                    yearValue = yearVal
                        addContribution = calcDyn(form.additionalContribution.data,month,year,timeframe)
                    decMonth = findDec(month)

                    

        
                    if intclass == "E":
                        thisinterest = interest.ClassE
                        calc = classE(month,year,value,fprofile,intclass,thisinterest,donation,recap,distribution,timeframe)
                    elif intclass == "F":
                        thisinterest = interest.ClassF
                        calc = classF(month,year,value,fprofile,intclass,thisinterest,donation,recap,operatingDistribution,timeframe)
                    elif intclass == "G" :
                        thisinterest = interest.ClassG
                        calc = classG(month,year,value,fprofile,intclass,thisinterest,donation,recap,operatingDistribution,timeframe)
                    elif(intclass == "H"):
                        thisinterest = interest.ClassH
                        calc = classH(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
                    elif intclass == "A":
                        thisinterest = interest.ClassA
                        calc = classA(month,year,value,fprofile,intclass,thisinterest,spending,recap,operatingDistribution,timeframe)
                    elif(intclass == "N"):
                        thisinterest = interest.ClassN
                        calc = classN(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
                    elif(intclass == "Q"):
                        thisinterest = interest.ClassQ
                        calc = classQ(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
                    elif(intclass == "S"):
                        thisinterest = interest.ClassS
                        calc = classS(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
                    savedata = form.savedata.data
                    if(savedata == True and current_user.is_authenticated):
                        clientsave = expected(user_id=int(current_user.id),month=str(form.month.data),year=int(form.year.data),
                        interest=thisinterest, value=int(form.fundvalue.data),intclass=str(form.interestClass.data),
                        donation=str(form.donation.data),spending=str(form.spending.data),
                        recap=str(form.recap.data),distribution=str(form.distribution.data),
                        operatingDistribution=str(form.operatingDistribution.data),
                        timeframe=int(form.timeframe.data),addContribution=str(form.additionalContribution.data))
                        db.session.add(clientsave)
                        db.session.commit()
                    
                    return render_template("calcs.html", title='Calculation Page', form=form, calc=calc, years=year,timeframe=timeframe,decMonth = decMonth,spending =spending,error = {})
                except:
                    error = {}
                    traceback.print_exc() #To print error Trace
                    month = form.month.data.strip().lower()
                    if month != 'dec' and month != 'nov' and month != 'oct' and month != 'sep' and month != 'aug' and month != 'jul' and month != 'jun' and month != 'may' and month != 'apr' and month != 'mar' and month != 'feb' and month != 'jan':
                        error["month"] = True
                    year = form.year.data
                    if len(str(year)) != 4:
                        error["year"] = True

                    if form.donation.data != '' and form.donation.data != '0' :
                        dynVal = form.donation.data.split(',')
                        yearValue = 0
                        for group in dynVal:
                            grpLst = group.split("-")
                            monthVal = grpLst[0].strip().lower()
                            if monthVal != 'dec' and monthVal != 'nov' and monthVal != 'oct' and monthVal != 'sep' and monthVal != 'aug' and monthVal != 'jul' and monthVal != 'jun' and monthVal != 'may' and monthVal != 'apr' and monthVal != 'mar' and monthVal != 'feb' and monthVal != 'jan':
                                error["donation"] = True
                            yearVal = grpLst[1].strip()
                            if len(str(yearVal)) != 4 or yearVal.isdigit() is False:
                                error["donation"] = True
                            elif yearVal.isdigit() == True :
                                if int(yearVal) < int(yearValue) :
                                    error["donation"] = True
                                    print(yearVal, yearValue)
                                    yearVal = 0
                                    
                                else:
                                    yearValue = yearVal
                            moneyVal = grpLst[2].strip()
                            if moneyVal.isdigit() is False:
                                error["donation"] = True
                    
                    if form.spending.data != '' and form.spending.data != '0' :
                        dynVal = form.spending.data.split(',')
                        yearValue = 0
                        for group in dynVal:
                            grpLst = group.split("-")
                            monthVal = grpLst[0].strip().lower()
                            if monthVal != 'dec' and monthVal != 'nov' and monthVal != 'oct' and monthVal != 'sep' and monthVal != 'aug' and monthVal != 'jul' and monthVal != 'jun' and monthVal != 'may' and monthVal != 'apr' and monthVal != 'mar' and monthVal != 'feb' and monthVal != 'jan':
                                error["spending"] = True
                            yearVal = grpLst[1].strip()
                            if len(str(yearVal)) != 4 or yearVal.isdigit() is False:
                                error["spending"] = True
                            elif yearVal.isdigit() == True :
                                if int(yearVal) < int(yearValue) :
                                    error["spending"] = True
                                    print(yearVal, yearValue)
                                    yearVal = 0
                                    
                                else:
                                    yearValue = yearVal
                            moneyVal = grpLst[2].strip()
                            if moneyVal.isdigit() is False:
                                error["spending"] = True

                    if form.recap.data != '' and form.recap.data != '0' :
                        dynVal = form.recap.data.split(',')
                        yearValue = 0
                        for group in dynVal:
                            grpLst = group.split("-")
                            monthVal = grpLst[0].strip().lower()
                            if monthVal != 'dec' and monthVal != 'nov' and monthVal != 'oct' and monthVal != 'sep' and monthVal != 'aug' and monthVal != 'jul' and monthVal != 'jun' and monthVal != 'may' and monthVal != 'apr' and monthVal != 'mar' and monthVal != 'feb' and monthVal != 'jan':
                                error["recap"] = True
                            yearVal = grpLst[1].strip()
                            print(yearVal.isdigit())
                            if len(str(yearVal)) != 4 or yearVal.isdigit() is False:
                                error["recap"] = True
                            elif yearVal.isdigit() == True :
                                if int(yearVal) < int(yearValue) :
                                    error["recap"] = True
                                    print(yearVal, yearValue)
                                    yearVal = 0
                                    
                                else:
                                    yearValue = yearVal
                            moneyVal = grpLst[2].strip()
                            if moneyVal.isdigit() is False:
                                error["recap"] = True

                    if form.operatingDistribution.data != '' and form.operatingDistribution.data != '0' :
                        dynVal = form.operatingDistribution.data.split(',')
                        yearValue = 0
                        for group in dynVal:
                            grpLst = group.split("-")
                            monthVal = grpLst[0].strip().lower()
                            if monthVal != 'dec' and monthVal != 'nov' and monthVal != 'oct' and monthVal != 'sep' and monthVal != 'aug' and monthVal != 'jul' and monthVal != 'jun' and monthVal != 'may' and monthVal != 'apr' and monthVal != 'mar' and monthVal != 'feb' and monthVal != 'jan':
                                error["operatingDistribution"] = True
                            yearVal = grpLst[1].strip()
                            print(yearVal.isdigit())
                            if len(str(yearVal)) != 4 or yearVal.isdigit() is False:
                                error["operatingDistribution"] = True
                            elif yearVal.isdigit() == True :
                                if int(yearVal) < int(yearValue) :
                                    error["operatingDistribution"] = True
                                    print(yearVal, yearValue)
                                    yearVal = 0
                                    
                                else:
                                    yearValue = yearVal
                            moneyVal = grpLst[2].strip()
                            if moneyVal.isdigit() is False:
                                error["operatingDistribution"] = True
                        
                    if form.additionalContribution.data != '' and form.additionalContribution.data != '0' :
                        dynVal = form.additionalContribution.data.split(',')
                        yearValue = 0
                        for group in dynVal:
                            grpLst = group.split("-")
                            monthVal = grpLst[0].strip().lower()
                            if monthVal != 'dec' and monthVal != 'nov' and monthVal != 'oct' and monthVal != 'sep' and monthVal != 'aug' and monthVal != 'jul' and monthVal != 'jun' and monthVal != 'may' and monthVal != 'apr' and monthVal != 'mar' and monthVal != 'feb' and monthVal != 'jan':
                                error["additionalContribution"] = True
                            yearVal = grpLst[1].strip()
                            print(yearVal.isdigit())
                            if len(str(yearVal)) != 4 or yearVal.isdigit() is False:
                                error["additionalContribution"] = True
                            elif yearVal.isdigit() == True :
                                if int(yearVal) < int(yearValue) :
                                    error["additionalContribution"] = True
                                    print(yearVal, yearValue)
                                    yearVal = 0
                                    
                                else:
                                    yearValue = yearVal
                            moneyVal = grpLst[2].strip()
                            if moneyVal.isdigit() is False:
                                error["additionalContribution"] = True
                    else:
                        error["funny"] = True
                        
                    return render_template("calcs.html", title='Calculation Page', error = error,form=form,calc = [[0],[0]],timeframe = 0,years=0,decMonth = 0,spending = 0)                
            return pdfGen()

    
    form = calculationForm()
 
    return render_template("calcs.html", title='Calculation Page', form=form,calc = [[0],[0]],timeframe = 0,years=0,decMonth = 0,spending = 0,error = {})


@app.route('/profile',methods=["GET", "POST"])
def profile():
    form1 = RemovalForm()
    form2 = storedSelect()
    
    if form1.validate_on_submit() and request.form['btn']=='form1':
        thisdata = form1.rid.data
        temp = expected.query.get(thisdata)
        print(temp)
        if(temp.user_id == current_user.id):
            db.session.delete(temp)
            db.session.commit()
        else:
            flash("You tried to remove a post that either does not belong to you or does not exist!")
        
        return redirect(url_for('profile'))

    

    if form2.validate_on_submit() and request.form['btn']=='form2':
        data = expected.query.get(form2.storedid.data)
        if(data.user_id == current_user.id and form2.storedid.data == data.id):
            month = str(data.month)
            year = int(data.year)
            value = int(data.value)
            intclass = str(data.intclass)
            thisinterest = float(data.interest)
            spending = int(data.spending)
            fprofile = None
            timeframe = int(data.timeframe)
            distribution = float(data.distribution)
            donation = data.donation
            spending = data.spending
            recap = data.recap
            operatingDistribution = data.operatingDistribution
            addContribution = data.addContribution

            
            if donation == '' or donation == '0':
                donation = {}
            else:
                dynVal = donation.split(',')
                yearValue = 0
                for group in dynVal:
                    grpLst = group.split("-")
                    monthVal = grpLst[0].strip().lower()
                    yearVal = grpLst[1].strip()
                    if yearVal.isdigit() == True :
                        if int(yearVal) < int(yearValue) :
                            raise Exception("Year 2 is lower than year 1")
                        else:
                            yearValue = yearVal
                donation = calcDyn(donation,month,year,timeframe)

            if spending == '' or spending == '0' :
                spending = {}
            else:
                dynVal = spending.split(',')
                yearValue = 0
                for group in dynVal:
                    grpLst = group.split("-")
                    monthVal = grpLst[0].strip().lower()
                    yearVal = grpLst[1].strip()
                    if yearVal.isdigit() == True :
                        if int(yearVal) < int(yearValue) :
                            raise Exception("Year 2 is lower than year 1")
                        else:
                            yearValue = yearVal
                        spending = calcDyn(spending,month,year,timeframe)

            if recap == '' or recap == '0':
                recap = {}
            else:
                dynVal = recap.split(',')
                yearValue = 0
                for group in dynVal:
                    grpLst = group.split("-")
                    monthVal = grpLst[0].strip().lower()
                    yearVal = grpLst[1].strip()
                    if yearVal.isdigit() == True :
                        if int(yearVal) < int(yearValue) :
                            raise Exception("Year 2 is lower than year 1")
                        else:
                            yearValue = yearVal
                recap = calcDyn(recap,month,year,timeframe)
                    
            if operatingDistribution == '' or operatingDistribution == '0' :
                operatingDistribution = {}
            else:
                dynVal = operatingDistribution.split(',')
                yearValue = 0
                for group in dynVal:
                    grpLst = group.split("-")
                    monthVal = grpLst[0].strip().lower()
                    yearVal = grpLst[1].strip()
                          
                    if yearVal.isdigit() == True :
                        if int(yearVal) < int(yearValue) :
                            raise Exception("Year 2 is lower than year 1")
                        else:
                            yearValue = yearVal
                operatingDistribution = calcDyn(operatingDistribution,month,year,timeframe)
                    
            if addContribution == '' or addContribution == '0':
                addContribution = {}
            else:
                dynVal = addContribution.split(',')
                yearValue = 0
                for group in dynVal:
                    grpLst = group.split("-")
                    monthVal = grpLst[0].strip().lower()
                    yearVal = grpLst[1].strip()
                    if yearVal.isdigit() == True :
                        if int(yearVal) < int(yearValue) :
                            raise Exception("Year 2 is lower than year 1")
                        else:
                            yearValue = yearVal
                addContribution = calcDyn(addContribution,month,year,timeframe)
            decMonth = findDec(month)


            if intclass == "E":
                calc = classE(month,year,value,fprofile,intclass,thisinterest,donation,recap,distribution,timeframe)
                return render_template("profile.html", title='Profile', expected=expected.query.all(), form=form1, form2=form2, calc=calc,timeframe = 0,years=0,decMonth = 0,spending = 0,error = {})
            elif intclass == "F":
                calc = classF(month,year,value,fprofile,intclass,thisinterest,donation,recap,operatingDistribution,timeframe)
                return render_template("profile.html", title='Profile', expected=expected.query.all(), form=form1, form2=form2, calc=calc,timeframe = 0,years=0,decMonth = 0,spending = 0,error = {})
            elif intclass == "G" :
                calc = classG(month,year,value,fprofile,intclass,thisinterest,donation,recap,operatingDistribution,timeframe)
                return render_template("profile.html", title='Profile', expected=expected.query.all(), form=form1, form2=form2,calc=calc,timeframe = 0,years=0,decMonth = 0,spending = 0,error = {})
            elif(intclass == "H"):
                calc = classH(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
                return render_template("profile.html", title='Profile', expected=expected.query.all(), form=form1, form2=form2,calc=calc,timeframe = 0,years=0,decMonth = 0,spending = 0,error = {})
            elif intclass == "A":
                calc = classA(month,year,value,fprofile,intclass,thisinterest,spending,recap,operatingDistribution,timeframe)
                return render_template("profile.html", title='Profile', expected=expected.query.all(), form=form1, form2=form2,calc=calc,timeframe = 0,years=0,decMonth = 0,spending = 0,error = {})
            elif(intclass == "N"):
                calc = classN(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
                return render_template("profile.html", title='Profile', expected=expected.query.all(), form=form1, form2=form2,calc=calc,timeframe = 0,years=0,decMonth = 0,spending = 0,error = {})
            elif(intclass == "Q"):
                calc = classQ(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
                return render_template("profile.html", title='Profile', expected=expected.query.all(), form=form1, form2=form2,calc=calc,timeframe = 0,years=0,decMonth = 0,spending = 0,error = {})
            elif(intclass == "S"):
                calc = classS(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
                return render_template("profile.html", title='Profile', expected=expected.query.all(), form=form1, form2=form2,calc=calc,timeframe = 0,years=0,decMonth = 0,spending = 0,error = {})

    return render_template("profile.html", title='Profile', expected=expected.query.all(), form=form1, form2=form2, calc = [[0],[0]],timeframe = 0,years=0,decMonth = 0,spending = 0,error = {})


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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('signin'))
    return render_template('register.html', title='Register New User', form=form)


@app.route('/reset', methods=['GET', 'POST'])
def reset():
	form = ResetPassword()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.currentPassword.data):
			flash('Invalid username or current password')
			return redirect(url_for('reset'))
		user.set_password(form.newPassword.data)
		db.session.commit()
		return redirect(url_for('signin'))
	return render_template('reset.html', title='Reset Password', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = InterestRatesForm()
    Interest = InterestRates.query.first()
    if form.validate_on_submit():
        if(form.ClassE.data != ''):
            Interest.ClassE = float(form.ClassE.data)

        if(form.ClassF.data != ''):
            Interest.ClassF = float(form.ClassF.data)

        if(form.ClassG.data != ''):
            Interest.ClassG = float(form.ClassG.data)

        if(form.ClassH.data != ''):
            Interest.ClassH = float(form.ClassH.data)

        if(form.ClassA.data != ''):
            Interest.ClassA = float(form.ClassA.data)

        if(form.ClassN.data != ''):
            Interest.ClassN = float(form.ClassN.data)

        if(form.ClassQ.data != ''):
            Interest.ClassQ = float(form.ClassQ.data)

        if(form.ClassS.data != ''):
            Interest.ClassS = float(form.ClassS.data)

        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('admin.html', title='Admin', form=form, Interest=Interest)

@app.route('/makeadmin', methods=['GET', 'POST'])
def makeadmin():
    form = makeAdmin()
    if form.validate_on_submit():
        temp = User.query.get(form.adminid.data)
        temp.admin = True
        db.session.add(temp)
        db.session.commit()
        return redirect(url_for('makeadmin'))
    return render_template('makeadmin.html', title='Make Admin', form=form)

@app.route('/adminreset', methods=['GET', 'POST'])
def adminreset():
	form = ForgottenPassword()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		user.set_password(form.newPassword.data)
		db.session.commit()
		return redirect(url_for('homepage'))
	return render_template('adminreset.html', title='Forgotten Password', form=form)
