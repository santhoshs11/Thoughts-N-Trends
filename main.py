from flask import Flask,redirect,render_template,request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String,Integer,Float
from flask_login import LoginManager


app=Flask(__name__)
Bootstrap5(app)



class Base(DeclarativeBase):
    pass




@app.route('/')
def home():
    return render_template('home.html')



if __name__=='__main__':
    app.run(debug=True)