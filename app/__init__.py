from flask import Flask

app = Flask(__name__) #create application object
app.config.from_object('config')

from app import views