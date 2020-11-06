from app import app
from flask import render_template
from app.routes import LoginForm

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
    

    