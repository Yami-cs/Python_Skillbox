from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired, ValidationError

# Создаем Flask-приложение
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'  # Замените на свой секретный ключ

# Валидатор для длины числа в виде класса
class NumberLength:
    def __init__(self, min_length, max_length, message=None):
        self.min_length = min_length
        self.max_length = max_length
        self.message = message

    def __call__(self, form, field):
        value = field.data
        if value is not None:
            value_str = str(value)
            if len(value_str) < self.min_length or len(value_str) > self.max_length:
                raise ValidationError(self.message or f"Number must be between {self.min_length} and {self.max_length} digits.")

# Создаем форму
class MyForm(FlaskForm):
    phone = IntegerField(validators=[InputRequired(), NumberLength(min_length=7, max_length=10, message="Invalid phone number")])

# Роут для отображения формы
@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        # Обработка данных формы
        phone_number = form.phone.data
        # Дополнительные действия с номером телефона
        return f"Phone number submitted: {phone_number}"
    return render_template('index.html', form=form)

# Второй роут для другой реализации валидатора
@app.route('/other', methods=['GET', 'POST'])
def other():
    form = MyForm()
    if form.validate_on_submit():
        # Обработка данных формы
        phone_number = form.phone.data
        # Дополнительные действия с номером телефона
        return f"Phone number submitted (other route): {phone_number}"
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
