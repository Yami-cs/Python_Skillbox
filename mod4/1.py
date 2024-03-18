from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class RegistrationForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    phone = StringField('Phone', [validators.DataRequired(), validators.Length(min=10, max=10), validators.Regexp(r'^\d+$', message="Только положительные числа")])
    name = StringField('Name', [validators.DataRequired()])
    address = StringField('Address', [validators.DataRequired()])
    index = IntegerField('Index', [validators.DataRequired()])
    comment = StringField('Comment')
