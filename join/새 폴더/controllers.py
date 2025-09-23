from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, logout_user

from auth import SHA256, already_signin
from forms import SignInForm, SignUpForm
from database.models import User
from database.session import db

app = Blueprint('users', __name__, url_prefix='/users')

@app.route('/signup', methods = ['GET', 'POST'])
@already_signin
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        id_user = User.query.filter(User.id == form.id.data).first()
        nickname_user = User.query.filter(User.nickname == form.nickname.data).first()
        if id_user:
            if id_user.id == form.id.data:
                form.id.erros.append('이미 가입된 아이디입니다.')
        if form.id.errors or form.nickname.erros:
            return render_template('signup.html', form=form)

        user = User(id=form.id.data, nickname=form.nickname.data, password=SHA256.encrypt(form.password.data))
        db.session.add(user)
        db.session.commit()

        login_user(user)
        return redirect(url_for('showtimes.index'))
    return render_template('signup.html', form=form)


@app.route('/signin', methods = ['GET', 'POST'])
@already_signin
def signin():
    form = SignInForm()

    if form.validate_on_submit():
        user = User.query.filter(User.id == form.id.data).first()
        if not user:
            form.id.errors.append('가입하지 않은 아이디입니다.')
            return render_template('signin.html', form = form)
        if user.password != SHA256.encrypt(form.password.data):
            form.password.errors.append('비밀번호가 일치하지 않습니다.')
            return render_template('signin.html', form=form)

        login_user(user)
        return redirect(url_for('showtimes.index'))
    return render_template('signin.html', form=form)


@app.route('signout', methods = ['GET'])
def signout():
    logout_user()
    return redirect(url_for('users.signin'))