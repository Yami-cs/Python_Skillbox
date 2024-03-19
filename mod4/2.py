from wtforms import ValidationError
from wtforms.validators import InputRequired

def number_length(min_length, max_length, message=None):
    def _number_length(form, field):
        if not (min_length <= len(str(field.data)) <= max_length):
            raise ValidationError(message or f"Поле должно содержать от {min_length} до {max_length} символов.")
    return _number_length

class NumberLength:
    def __init__(self, min_length, max_length, message=None):
        self.min_length = min_length
        self.max_length = max_length
        self.message = message

    def __call__(self, form, field):
        if not (self.min_length <= len(str(field.data)) <= self.max_length):
            raise ValidationError(self.message or f"Поле должно содержать от {self.min_length} до {self.max_length} символов.")

# Пример использования
from flask_wtf import FlaskForm
from wtforms import IntegerField

class MyForm(FlaskForm):
    phone1 = IntegerField(validators=[InputRequired(), number_length(min_length=5, max_length=10)])
    phone2 = IntegerField(validators=[InputRequired(), NumberLength(min_length=5, max_length=10)])
