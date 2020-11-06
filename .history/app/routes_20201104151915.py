from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ernest'}

    posts = [
        {
            'author': {'username': 'Lanre'},
            'body': 'Beautiful day at Hub 67'},

        {
            'author': {'username': 'Ayomikun'},
            'body': 'She is a backend developer'}
    ]
    return render_template('index.html',title = 'Home', user = user, posts = posts)
    

@app.route('/login', methodd)
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect('/index')
    return render_template('login.html', title = 'Sign In', form = form)
    