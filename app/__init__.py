from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app: Flask = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db: SQLAlchemy = SQLAlchemy(app)

#from routes import routes

from flask import render_template, url_for, flash, redirect, request
#from . import app, db
# from app.forms import CredentialsForm
# from app.models import Credentials


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/post/new", methods=['POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        credentials = Credentials(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(credentials) # add item to the db
        db.session.commit() # save the item in the db
        flash('Your Credentials has been created!', 'success')
        return redirect(url_for('home'))
    return redirect(url_for('home')) # you can send an error page or to the same page