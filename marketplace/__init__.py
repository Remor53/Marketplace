from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///avito_adv_old.db'
app.config['SECRET_KEY'] = 'glassesdata'
db = SQLAlchemy(app)

from marketplace import routes
