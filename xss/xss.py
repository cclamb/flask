#
# http://localhost:5000/?user=<script>alert('foo');</script>
#
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def exploitable():
    payload = request.args.get('user')
    payload = payload if payload != None else 'no payload submitted'
    return payload
