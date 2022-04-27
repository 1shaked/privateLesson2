from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class CredentialsForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = TextAreaField('Password', validators=[DataRequired()])
    name = TextAreaField('Name')
    submit = SubmitField('Post')