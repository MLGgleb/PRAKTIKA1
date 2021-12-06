# -*- coding: utf-8 -*-
from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
 user = {'username': 'Gleb'}
 posts = [
  {
   'author': {'username': 'Johnny'},
   'body': 'What a lovely day!'
  },
  {
   'author': {'username': 'Саня'},
   'body': 'I speak English very well.'
  },
  {
   'author': {'username': 'Василий'},
   'body': 'Привет всем!!'
  },
  {
   'author': {'username': 'Peter'},
   'body': 'I like pizza!!!'
  }
 ]
 return render_template('index.html', title='Home', user=user, posts=posts)
