from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    phone = StringField('Phone', [validators.DataRequired(), validators.Length(min=10, max=10), validators.Regexp(r'^\d+$', message="Только положительные числа")])
    name = StringField('Name', [validators.DataRequired()])
    address = StringField('Address', [validators.DataRequired()])
    index = IntegerField('Index', [validators.DataRequired()])
    comment = StringField('Comment')

@app.route("/reg", methods=["POST"])
def reg():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Successfuly registered user {email} with phone +7{phone}"
    return f"Invalid input, {form.errors}", 400

if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)