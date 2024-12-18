from urllib.parse import quote

from flask import Flask
# from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
# import cloudinary

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{quote('admin123')}@localhost/clinic?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_PATIENTS_PER_DAY'] = 2
app.config['CURRENT_YEAR'] = 2024

db = SQLAlchemy(app=app)
# login = LoginManager(app=app)

