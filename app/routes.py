from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from werkzeug.urls import url_parse
from calculations.ClassHS import ClassHS
from calculations.ClassN import ClassN
from calculations.ClassQ import ClassQ
from calculations.classEFG import ClassEFG

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template("homepage.html", title='Home Page')

@app.route('/calc')
def calcs():
    return render_template("calcs.html", title='Calculation Page')

@app.route('/profile')
def profile():
    return render_template("profile.html", title='Profile')