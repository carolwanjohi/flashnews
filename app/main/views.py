from flask import render_template,request,redirect,url_for
from . import main

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message = "Hello World"
    return render_template('index.html', message=message)

@main.route('/source/source')
def source(source):
    '''
    View source oage function that returns a source page and its data
    '''
    message = f"You are viewing {source}"
    return render_template('source.html', message=message)
