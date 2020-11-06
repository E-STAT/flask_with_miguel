from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ernest'}

    posts = []
        'author': {'username': 'Lanre'},
        'body': 'Beautiful day at Hub 67'
    }
    return render_template('index.html', title = 'Home', user = user)
    

    