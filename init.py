from flask import Flask

#import the config object
from config import Config

#import for the SQLAlchemy Object
from flask_sqlalchemy import SQLAlchemy

#Import the Migrat Oject
from flask_migrate import Migrate

app = Flask(__name__)
# Complete the Config cycle to our own Flask App
# And give access to our database (when we have one)
# along with our Secret Key
app.config.from_object(Config)

#Init the database (db)
db = SQLAlchemy(app)

# Init the migrator
migrate = Migrate(app,db)

#Won't create the tables if this line is not present
from avengers_phone_book_app import routes,models