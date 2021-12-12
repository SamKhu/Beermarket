from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError
from beermarket.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user=User.query.filter_by(user_name=username_to_check.data).first()
        if user:
            raise ValidationError('Пользователь с таким именем уже существует, попробуйте другое')

    def validate_email(self, email_to_check):
        email=User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Адрес электронной почты уже используется, проверьте адрес почты')


    username=StringField(label='Имя Пользователя', validators=[Length(min=2, max=30),DataRequired()])
    email=StringField(label='Электронная почта', validators=[Email(), DataRequired()])
    password_1=PasswordField(label='Пароль', validators=[Length(min=6), DataRequired()])
    password_2=PasswordField(label='Подтверждение пароля', validators=[EqualTo('password_1'), DataRequired()])
    submit=SubmitField(label='Создать учётную запись')

class LoginForm(FlaskForm):
    username=StringField(label='Имя пользователя', validators=[DataRequired()])
    password=PasswordField(label='Пароль', validators=[DataRequired()])
    submit=SubmitField(label='Войти')