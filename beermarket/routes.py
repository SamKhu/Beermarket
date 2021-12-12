from beermarket import app, db
from flask import render_template, flash, redirect, url_for
from beermarket.models import Item, User
from beermarket.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/bar")
def bar_page():
    return render_template('bar.html')

@app.route("/draft")
def draft_page():
    return render_template('draft.html')

@app.route("/bottles")
def bottles_page():
    return render_template('bottles.html')

@app.route("/market")
@login_required
def market_page():
    items=Item.query.all()
    return render_template('market.html', items=items)

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form=RegisterForm()
    if form.validate_on_submit():
        user_to_create=User(
            user_name=form.username.data,
            email=form.email.data,
            password=form.password_1.data
        )
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Регистрация прошла успешно! Вы в системе под именем: {user_to_create.user_name}", category="success")


        return redirect (url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'При регистрации произошла ошибка: {err_msg}', category="danger")


    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form=LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(user_name=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Вы успешно  авторизовались, как {attempted_user.user_name}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Неудачная авторизация', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout_page():
    logout_user()
    return redirect(url_for('home_page'))
