from wtforms import ValidationError
from wtforms.validators import InputRequired

def number_length(min_length, max_length, message=None):
    def _number_length(form, field):
        if not (min_length <= len(str(field.data)) <= max_length):
            raise ValidationError(message or f"Поле должно содержать от {min_length} до {max_length} символов.")
    return _number_length

