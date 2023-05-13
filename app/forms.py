from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class PokemonLookUpForm(FlaskForm):
    name = StringField('Name', validators= [DataRequired()])
    