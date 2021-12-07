from beermarket import app, db
from flask import render_template, flash
from beermarket.forms import RegisterForm
from beermarket.models import Item, User
from flask import redirect, url_for

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
def market_page():
    items=Item.query.all()
    return render_template('market.html', items=items)

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form=RegisterForm()
    if form.validate_on_submit():
        user_to_create= User(
            user_name=form.username.data,
            email=form.email.data,
            password_hash=form.password_1.data
        )
        db.session.add(user_to_create)
        db.session.commit()
        return redirect (url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'При регистрации произошла ошибка: {err_msg}', category="danger")


    return render_template('register.html', form=form)