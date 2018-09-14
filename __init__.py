from flask import Flask
from App import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='templates',static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:78692746@127.0.0.1:3306/student"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(config)
db = SQLAlchemy(app)

from App import view