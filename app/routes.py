from flask import render_template, flash, redirect, url_for, request, make_response
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, InterestRates, expected
from app.forms import calculationForm, LoginForm, RegistrationForm, InterestRatesForm, RemovalForm, makeAdmin, ResetPassword, ForgottenPassword, storedSelect, compForm
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
from calculations.findMonth import findMonth
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
                    intMonth = findMonth(month)
                    year = form.year.data
                    if len(year) != 4 or year.isdigit() == False :
                        raise Exception("Invalid Years")
                    year = int(year)
                    value =  form.fundvalue.data
                    if value.isdigit() == False :
                        raise Exception("Invalid Fund Value")
                    value = int(value)
                    fprofile = None
                    intclass = form.interestClass.data.strip()
                    interest = InterestRates.query.first()
                    distribution = form.distribution.data
                    timeframe = form.timeframe.data
                    if timeframe.isdigit() == False :
                        raise Exception("Invalid Time Frame")
                    timeframe = int(timeframe)
                    
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
                        clientsave = expected(user_id=int(current_user.id), month=str(form.month.data),year=int(form.year.data),
                        interest=thisinterest, value=int(form.fundvalue.data),intclass=str(form.interestClass.data),
                        donation=str(form.donation.data),spending=str(form.spending.data),
                        recap=str(form.recap.data),distribution=str(form.distribution.data),
                        operatingDistribution=str(form.operatingDistribution.data),
                        timeframe= int(form.timeframe.data),
                        addContribution=str(form.additionalContribution.data),nickname=str(form.nickname.data))
                        db.session.add(clientsave)
                        db.session.commit()
                    
                    return render_template("calcs.html", title='Calculation Page', form=form, calc=calc, years=year,timeframe=timeframe,timeframe1=0, decMonth1=0, decMonth = decMonth,spending =spending,error = {},months = intMonth)
                except:
                    error = {}
                    traceback.print_exc() #To print error Trace
                    month = form.month.data.strip().lower()
                    if month != 'dec' and month != 'nov' and month != 'oct' and month != 'sep' and month != 'aug' and month != 'jul' and month != 'jun' and month != 'may' and month != 'apr' and month != 'mar' and month != 'feb' and month != 'jan':
                        error["month"] = True
                    year = form.year.data
                    if len(year) != 4 or year.isdigit() == False :
                        error["year"] = True
                    value = form.fundvalue.data
                    if value.isdigit() == False :
                        error["value"] = True
                    timeframe = form.timeframe.data
                    if timeframe.isdigit() == False :
                        error["timeframe"] = True

                    if form.donation.data != '' and form.donation.data != '0' :
                        dynVal = form.donation.data.split(',')
                        yearValue = 0
                        for group in dynVal:
                            grpLst = group.split("-")
                            if len(grpLst) != 3 :
                                error["donation"] = True
                            else:
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
                            if len(grpLst) != 3 :
                                error["spending"] = True
                            else:
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
                            if len(grpLst) != 3 :
                                error["recap"] = True
                            else:
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
                            if len(grpLst) != 3 :
                                error["operatingDistribution"] = True
                            else:
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
                            if len(grpLst) != 3 :
                                error["additionalContribution"] = True
                            else:
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
        else:
            form = calculationForm()
            return pdfGen(form.month.data,form.year.data,form.fundvalue.data,form.interestClass.data,form.donation.data,form.spending.data,form.recap.data,form.distribution.data,form.operatingDistribution.data,form.additionalContribution.data,form.timeframe.data)

    
    form = calculationForm()
 
    return render_template("calcs.html", title='Calculation Page', form=form,calc = [[0],[0]],timeframe = 0,years=0,decMonth = 0,spending = 0,error = None)


@app.route('/profile',methods=["GET", "POST"])
def profile():
    Remove = RemovalForm()
    View = storedSelect()
    Analyse = compForm()
    error = False
    error2 = False
    
    if Remove.validate_on_submit() and request.form['btn']=='Remove':
        error2=False
        thisdata = Remove.rid.data
        temp = expected.query.get(thisdata)
        if(temp != None and temp.user_id == current_user.id):
            db.session.delete(temp)
            db.session.commit()
        else:
            error2 = True
        
        return render_template("profile.html", title='Profile', expected=expected.query.all(), form=Remove, View=View, Analyse=Analyse, calc = [[0],[0]],calc3=[[0],[0]], calc4=[[0],[0]],timeframemax=0,timeframe = 0,years=0,decMonth = 0,spending = 0,timeframe1 = 0,years1=0,decMonth1 = 0,spending1 = 0,timeframe2 = 0,years2=0,decMonth2 = 0,spending2 = 0,error = {},error2=error2)

    

    if View.validate_on_submit() and request.form['btn']=='View':
        error2=False
        data = expected.query.get(View.storedid.data)
        if(data != None and data.user_id == current_user.id and View.storedid.data == data.id):  
        
            month = str(data.month)
            intMonth = findMonth(month)
            year = int(data.year)
            value = int(data.value)
            intclass = str(data.intclass)
            thisinterest = float(data.interest)
            spending = data.spending
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
                donation = calcDyn(data.donation,month,year,timeframe)

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
                        spending = calcDyn(data.spending,month,year,timeframe)

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
            elif intclass == "F":
                calc = classF(month,year,value,fprofile,intclass,thisinterest,donation,recap,operatingDistribution,timeframe)
            elif intclass == "G" :
                calc = classG(month,year,value,fprofile,intclass,thisinterest,donation,recap,operatingDistribution,timeframe)
            elif(intclass == "H"):
                calc = classH(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
            elif intclass == "A":
                calc = classA(month,year,value,fprofile,intclass,thisinterest,spending,recap,operatingDistribution,timeframe)
            elif(intclass == "N"):
                calc = classN(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
            elif(intclass == "Q"):
                calc = classQ(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
            elif(intclass == "S"):
                calc = classS(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)    
            
            return render_template("profile.html", title='Profile', expected=expected.query.all(),timeframemax=0, form=Remove, View=View,Analyse=Analyse,calc=calc,calc3=[[0],[0]], calc4=[[0],[0]],timeframe=timeframe,years=year,decMonth = decMonth,spending = spending,timeframe1 = 0,intclass = intclass,years1=0,decMonth1 = 0,spending1 = 0,timeframe2 = 0,years2=0,decMonth2 = 0,spending2 = 0,error = False, error2=error2,months = intMonth)
        else:
            error2 = True
            return render_template("profile.html", title='Profile', expected=expected.query.all(),timeframemax=0, form=Remove, View=View,Analyse=Analyse,calc=[[0],[0]],calc3=[[0],[0]], calc4=[[0],[0]],timeframe = 0,years=0,decMonth = 0,spending = 0,timeframe1 = 0,years1=0,decMonth1 = 0,spending1 = 0,timeframe2 = 0,years2=0,decMonth2 = 0,spending2 = 0,error = {}, error2=error2)
    
    if Analyse.validate_on_submit() and request.form['btn']=='Analyse':
        error2 = False
        data1 = expected.query.get(Analyse.stored1.data)
        data2 = expected.query.get(Analyse.stored2.data)
        if(data1 != None and data2 != None and data1.user_id == current_user.id and data2.user_id == current_user.id and Analyse.stored1.data == data1.id and Analyse.stored2.data == data2.id):    
            month1 = str(data1.month)
            intMonth1 = findMonth(month1)
            year1 = int(data1.year)
            value1 = int(data1.value)
            intclass1 = str(data1.intclass)
            thisinterest1 = float(data1.interest)
            spending1 = data1.spending
            title1 = str(data1.nickname)
            fprofile = None
            timeframe1 = int(data1.timeframe)
            distribution1 = float(data1.distribution)
            donation1 = data1.donation
            spending1 = data1.spending
            recap1 = data1.recap
            operatingDistribution1 = data1.operatingDistribution
            addContribution1 = data1.addContribution
            timeframemax = timeframe1

            if donation1 == '' or donation1 == '0':
                donation1 = {}
            else:
                dynVal = donation1.split(',')
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
                donation1 = calcDyn(data1.donation,month1,year1,timeframe1)

            if spending1 == '' or spending1 == '0' :
                spending1 = {}
            else:
                dynVal = spending1.split(',')
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
                        spending1 = calcDyn(data1.spending,month1,year1,timeframe1)

            if recap1 == '' or recap1 == '0':
                recap1 = {}
            else:
                dynVal = recap1.split(',')
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
                recap1 = calcDyn(recap1,month1,year1,timeframe1)
                    
            if operatingDistribution1 == '' or operatingDistribution1 == '0' :
                operatingDistribution1 = {}
            else:
                dynVal = operatingDistribution1.split(',')
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
                operatingDistribution1 = calcDyn(operatingDistribution1,month1,year1,timeframe1)
                    
            if addContribution1 == '' or addContribution1 == '0':
                addContribution1 = {}
            else:
                dynVal = addContribution1.split(',')
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
                addContribution1 = calcDyn(addContribution1,month1,year1,timeframe1)
            decMonth1 = findDec(month1)

            if intclass1 == "E":
                calc3 = classE(month1,year1,value1,fprofile,intclass1,thisinterest1,donation1,recap1,distribution1,timeframe1)
                
            elif intclass1 == "F":
                calc3 = classF(month1,year1,value1,fprofile,intclass1,thisinterest1,donation1,recap1,operatingDistribution1,timeframe1)
                
            elif intclass1 == "G" :
                calc3 = classG(month1,year1,value1,fprofile,intclass1,thisinterest1,donation1,recap1,operatingDistribution1,timeframe1)
                
            elif(intclass1 == "H"):
                calc3 = classH(month1,year1,value1,fprofile,intclass1,thisinterest1,spending1,addContribution1,timeframe1)
                
            elif intclass1 == "A":
                calc3 = classA(month1,year1,value1,fprofile,intclass1,thisinterest1,spending1,recap1,operatingDistribution1,timeframe1)
                
            elif(intclass1 == "N"):
                calc3 = classN(month1,year1,value1,fprofile,intclass1,thisinterest1,spending1,addContribution1,timeframe1)
                
            elif(intclass1 == "Q"):
                calc3 = classQ(month1,year1,value1,fprofile,intclass1,thisinterest1,spending1,addContribution1,timeframe1)
                
            elif(intclass1 == "S"):
                calc3 = classS(month1,year1,value1,fprofile,intclass1,thisinterest1,spending1,addContribution1,timeframe1)
                

            month2 = str(data2.month)
            intMonth2 = findMonth(month2)
            year2 = int(data2.year)
            title2 = str(data2.nickname)
            
            value2 = int(data2.value)
            intclass2 = str(data2.intclass)
            thisinterest2 = float(data2.interest)
            spending2 = data2.spending
            fprofile = None
            timeframe2 = int(data2.timeframe)
            if timeframe1<timeframe2:
                timeframemax = timeframe2
            distribution2 = float(data2.distribution)
            donation2 = data2.donation
            spending2 = data2.spending
            recap2 = data2.recap
            operatingDistribution2 = data2.operatingDistribution
            addContribution2 = data2.addContribution
            
            
            if donation2 == '' or donation2 == '0':
                donation2 = {}
            else:
                dynVal = donation2.split(',')
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
                donation2 = calcDyn(data2.donation,month2,year2,timeframe2)

            if spending2 == '' or spending2 == '0' :
                spending2 = {}
            else:
                dynVal = spending2.split(',')
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
                        spending2 = calcDyn(data2.spending,month2,year2,timeframe2)

            if recap2 == '' or recap2 == '0':
                recap2 = {}
            else:
                dynVal = recap2.split(',')
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
                recap2 = calcDyn(recap2,month2,year2,timeframe2)
                    
            if operatingDistribution2 == '' or operatingDistribution2 == '0' :
                operatingDistribution2 = {}
            else:
                dynVal = operatingDistribution2.split(',')
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
                operatingDistribution2 = calcDyn(operatingDistribution2,month2,year2,timeframe2)
                    
            if addContribution2 == '' or addContribution2 == '0':
                addContribution2 = {}
            else:
                dynVal = addContribution2.split(',')
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
                addContribution2 = calcDyn(addContribution2,month2,year2,timeframe2)
            decMonth2 = findDec(month2)

            if intclass2 == "E":
                calc4 = classE(month2,year2,value2,fprofile,intclass2,thisinterest2,donation2,recap2,distribution2,timeframe2)
                
            elif intclass2 == "F":
                calc4 = classF(month2,year2,value2,fprofile,intclass2,thisinterest2,donation2,recap2,operatingDistribution2,timeframe2)
                
            elif intclass2 == "G" :
                calc4 = classG(month2,year2,value2,fprofile,intclass2,thisinterest2,donation2,recap2,operatingDistribution2,timeframe2)
                
            elif(intclass2 == "H"):
                calc4 = classH(month2,year2,value2,fprofile,intclass2,thisinterest2,spending2,addContribution2,timeframe2)
                
            elif intclass2 == "A":
                calc4 = classA(month2,year2,value2,fprofile,intclass2,thisinterest2,spending2,recap2,operatingDistribution2,timeframe2)
               
            elif(intclass2 == "N"):
                calc4 = classN(month2,year2,value2,fprofile,intclass2,thisinterest2,spending2,addContribution2,timeframe2)
                
            elif(intclass2 == "Q"):
                calc4 = classQ(month2,year2,value2,fprofile,intclass2,thisinterest2,spending2,addContribution2,timeframe2)
                
            elif(intclass2 == "S"):
                calc4 = classS(month2,year2,value2,fprofile,intclass2,thisinterest2,spending2,addContribution2,timeframe2)
            # find greatest years
            
            
            return render_template("profile.html", title='Profile', title1=title1, title2=title2, expected=expected.query.all(), timeframemax=timeframemax, form=Remove, View=View,Analyse=Analyse, calc=[[0],[0]],calc3=calc3, calc4=calc4, timeframe=0,years=0,decMonth=0, timeframe1 = timeframe1, timeframe2=timeframe2,intclass1 = intclass1,intclass2 = intclass2,years1=year1,years2=year2,decMonth1 = decMonth1,decMonth2 = decMonth2,spending1 = spending1,spending2 = spending2,error = 'False3', error2=error2,months1 = intMonth1,months2 = intMonth2)
            
        else:   
            error2 = True
            return render_template("profile.html", title='Profile', title1=0, title2=0,expected=expected.query.all(),timeframemax=0, form=Remove, View=View, Analyse=Analyse, calc = [[0],[0]],calc3=[[1],[0]], calc4=[[1],[0]],timeframe=0,years=year,decMonth=0,timeframe1 = 0,years1=0,decMonth1 = 0,spending1 = 0,timeframe2 = 0,years2=0,decMonth2 = 0,spending2 = 0,error = {}, error2=error2)

    error2=False
    return render_template("profile.html", title='Profile',title1=0, title2=0, expected=expected.query.all(),timeframemax=0, form=Remove, View=View, Analyse=Analyse, calc = [[0],[0]],calc3=[[0],[0]], calc4=[[0],[0]],timeframe=0,years=0,decMonth=0,timeframe1 = 0,years1=0,decMonth1 = 0,spending1 = 0,timeframe2 = 0,years2=0,decMonth2 = 0,spending2= 0,error = {}, error2=error2)


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
        if (user == None):
            return render_template('reset.html', title='Reset Password', form=form, error = True, error2 =False)
        elif (user!=None and not user.check_password(form.currentPassword.data)):
            return render_template('reset.html', title='Reset Password', form=form, error = True, error2 =False)


        if (form.newPassword.data == form.newPassword2.data):
            user.set_password(form.newPassword.data)
            db.session.commit()
            return redirect(url_for('reset'))
        else:
            return render_template('reset.html', title='Reset Password', form=form, error = False, error2 =True)
    return render_template('reset.html', title='Reset Password', form=form, error = False, error2 =False)



	# 	if user is None or not user.check_password(form.currentPassword.data):
	# 		return redirect(url_for('reset'))
	# 	user.set_password(form.newPassword.data)
	# 	db.session.commit()
	# 	return redirect(url_for('signin'))
	# return render_template('reset.html', title='Reset Password', form=form)


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
    form = ResetPassword()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if (user != None):
            if (form.newPassword.data != form.newPassword2.data):
                 return render_template('adminreset.html', title='Forgotten Password', form=form, error = False, error2 =True)
            user.set_password(form.newPassword.data)
            db.session.commit()
            return redirect(url_for('homepage'))
        else:
            return render_template('adminreset.html', title='Forgotten Password', form=form, error = True, error2 =False)
    return render_template('adminreset.html', title='Forgotten Password', form=form, error = False, error2 =False)

@app.route('/userlist', methods=['GET', 'POST'])
def userlist():
    return render_template('userlist.html', User=User.query.all())
