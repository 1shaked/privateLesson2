from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
app: Flask = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///credentials.db'
db: SQLAlchemy = SQLAlchemy(app)
#from routes import routes

from flask import render_template, url_for, flash, redirect, request
#from . import app, db
# from .forms import CredentialsForm
# from app.models import Credentials
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class Credentials(db.Model):
    email = db.Column(db.String(100))
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100),  nullable=True)
    site = db.Column(db.String(100),  nullable=False)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    def __repr__(self):
        return f"Post('{self.email}', '{self.password}')"
class CredentialsForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = TextAreaField('Password', validators=[DataRequired()])
    name = TextAreaField('Name')
    submit = SubmitField('Post')



names = db.engine.table_names()
print(names)
db.create_all()
db.session.commit()
@app.route("/")
@app.route("/home")
def home():
    df = pd.read_sql_table(table_name='credentials', con=db.engine)
    print(df)
    return render_template('home.html')

@app.route("/post/new", methods=['POST'])
def new_post():
    form = CredentialsForm()
    print(form)

    credentials = Credentials(email=form.email.data, password=form.password.data, name=form.name.data,site='s' )
    db.session.add(credentials) # add item to the db
    db.session.commit() # save the item in the db
    flash('Your Credentials has been created!', 'success')

    '''
    if form.validate_on_submit():
        credentials = Credentials(email=form.email.data, password=form.password.data, name=form.name.data)
        db.session.add(credentials) # add item to the db
        db.session.commit() # save the item in the db
        flash('Your Credentials has been created!', 'success')
        return redirect(url_for('home'))
    '''
    return redirect(url_for('home')) # you can send an error page or to the same page