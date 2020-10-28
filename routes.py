#import the app variable from the init 
from avengers_phone_book_app import app

#Import Our Form(s)
from flask import render_template, request

#import specific packages from flask
from flask import render_template


# Import specific packages from flask
from flask import render_template

# Import Our Form(s)
from avengers_phone_book_app.forms import UserInfoForm

#Default Home Route
@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/test')
def testRoute():
    names = ['Thor', 'Black_Panther', 'Captain_America', 'Hulk']
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
        phone = form.phone.data
        email = form.email.data
        password = form.password.data
        #print the data to the server that comes from the form
        print(username,email,password)

    return render_template('register,html', user_form = form)