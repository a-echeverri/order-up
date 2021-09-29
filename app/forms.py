from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields import BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
from wtforms.widgets.html5 import DateInput, TimeInput

class LoginForm(FlaskForm):
    employee_number = StringField(''
    )