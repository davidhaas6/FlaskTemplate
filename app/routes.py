from flask import render_template, flash, redirect, url_for, request, g, jsonify, abort
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
from app import app, db
from config import Config

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='')
