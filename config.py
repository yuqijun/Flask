import os
from datetime import timedelta
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:78692746@127.0.0.1:3306/student"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY =  "123456"    #os.urandom(20)
PERMANENT_SESSION_LIFETIME = timedelta(days=7)
