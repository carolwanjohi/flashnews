from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = "FlashNews"
    sources = get_sources()
    return render_template('index.html', title=title, sources=sources)

@main.route('/source/<source_name>')
def source(source_name):
    '''
    View source page function that returns a source page and its data
    '''
    title = f"{source_name} Page"
    message = f"You are viewing {source_name}"
    return render_template('source.html', title=title, message=message)
