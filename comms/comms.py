#
# http://localhost:5000/?user=<script>alert('foo');</script>
#
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def exploitable():
    payload = request.args.get('id')
    payload = payload if payload != None else 'no payload submitted'
    return render_template('index.html', user=payload)
