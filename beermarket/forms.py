from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, Email, EqualTo

class RegisterForm(FlaskForm):
    username=StringField(label='Имя Пользователя', validators=[Length(min=2, max=30),DataRequired()])
    email=StringField(label='Электронная почта', validators=[Email(), DataRequired()])
    password_1=PasswordField(label='Пароль', validators=[Length(min=6), DataRequired()])
    password_2=PasswordField(label='Подтверждение пароля', validators=[EqualTo('password_1'), DataRequired()])
    submit=SubmitField(label='Создать учётную запись')