
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Pet Species", validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'])])
    photo = StringField("Pet Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Pet Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes for Pet", validators=[Optional()])

class EditPetForm(FlaskForm):
    photo = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes")
    available = BooleanField("Available")