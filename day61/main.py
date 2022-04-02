from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = "my-secret-key"
Bootstrap(app)


class Form(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Log in")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    email = None
    password = None
    form = Form()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email == 'admin@email.com' and password == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template("login.html",
                           email=email,
                           password=password,
                           form=form)


if __name__ == '__main__':
    app.run(debug=True)
