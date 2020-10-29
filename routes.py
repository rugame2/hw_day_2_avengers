#import the app variable from the init 
from hw_day_2_avengers_app import app, db

#Import Our Form(s)
from flask import render_template, request, redirect, url_for

# import our forms
from hw_day_2_avengers_app.forms import UserInfoForm, LoginForm

#Import models for the data base
from hw_day_2_avengers_app.models import User, Post, check_password_hash

#Import for flask lolgin functions login required
# login_user, current_user, logout_user
from flask_login import login_required, login_user, current_user, logout_user

# Import specific packages from flask
from flask import render_template

# Import Our Form(s)
from hw_day_2_avengers_app.forms import UserInfoForm

#Default Home Route
@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/test')
def testRoute():
    names = ['Hulk','Thor','Captain_America','Black_Panther']
    return render_template('test.html',list_names = names)


# GET == Gathering information
# POST == Sending Information
@app.route('/register', methods = ['GET', 'POST'])
def register():
    #Init our Form
    form = UserInfoForm()
    #Validation of our form
    if request.method == 'POST' and form.validate():
        # Get information from the form
        username = form.username.data
        email = form.email.data
        password = form.password.data
        #print the data to the server that comes from the form
        print(username,email,password)

        # Creation/init of our User Class (aka Model)
        user = User(username,email,password)

        #Open a connection to the database
        db.session.add(user)

        # Commit all data to the database
        db.session.commit()
    
    return render_template('register.html', user_form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method  == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
            
        #Saving the logged in user to a variable
        logged_user = User.query.filter(User.email == email).first()
        # check the password of the newly found user
        # and validate the password against the hash value
        # inside of the database
        print(logged_user.email)
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            return redirect(url_for('home'))
        else:
            return 'Not Logged In'
    return render_template('login.html', login_form = form) 