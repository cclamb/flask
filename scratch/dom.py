#
# http://localhost:5000/?user=<script>alert('foo');</script>
#
import os

from flask import Flask
from flask import request
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def exploitable():
    payload = request.args.get('id')
    payload = payload if payload != None else 'no payload submitted'
    return render_template('index.html', user=payload)
