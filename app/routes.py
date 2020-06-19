from app import app, db
from flask import render_template, redirect, url_for, session
from app.models import User, Post
from app.forms import RegistrationForm, LoginForm


@app.route('/')
def index():
    email = session.get('email', False)
    return render_template('index.html', email=email)


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()
    if form.validate_on_submit():
        register_data = {
            'name': form.name.data,
            'email': form.email.data,
            'age': form.age.data,
            'sex': form.sex.data,
            'password': form.password.data,
            'about_me': form.about_me.data,
        }
        if User.query.filter(User.email == register_data['email']).one_or_none() is not None:
            return render_template('registration.html', form=form, error="Такой пользователь уже существует!")
        new_user = User(
            email=register_data['email'],
            password=register_data['password'],
            name=register_data['name'],
        )
        session['email'] = register_data['email']
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('registration.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_data = {
            'email': form.email.data,
            'password': form.password.data,
            'remember_me': form.remember_me.data
        }
        user_db = User.query.filter(User.email == login_data['email']).one_or_none()
        if getattr(user_db, 'password', None) != login_data['password']:
            return render_template('login.html', title='Войти на сайт', form=form,
                                   error="Неправильный логин или пароль!")
        session['email'] = login_data['email']
        return redirect(url_for('index'))
    return render_template('login.html', title='Войти на сайт', form=form)