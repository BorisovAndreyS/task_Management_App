from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://taskuser:taskpassword@database:5432/taskdb'
db = SQLAlchemy(app)

from app import routes
