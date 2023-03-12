#! /usr/bin/python3
from flask import Flask,redirect
from markupsafe import escape
import os
from goto import *
import settings




app = Flask(__name__)
settings.init()


@app.route('/')
def index():
     return redirect("http://www.google.com", code=302)


@app.route('/<alias>')
def goto(alias):
     return redirect(settings.urls[alias.lower()], code=302)

@app.route('/list')
@app.route('/ls')
@app.route('/l')
def ls():
     return list()


@app.route('/add/<alias>/<url>')
def add_url(alias,url):
     return goto.add(alias,url)

@app.route('/p/<p>')
@app.route('/profile/<p>')
def prof(p=None):
     return profile(p)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)