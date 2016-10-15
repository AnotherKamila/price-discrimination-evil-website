"""Returns a different response based on whether this site was visited before.

Uses a simple cookie.
"""

from flask import Flask, make_response, request, url_for
app = Flask(__name__)

@app.route('/')
def simple_cookie():
    img = '2.jpg' if 'visited' in request.cookies else '1.jpg'
    resp = make_response('<img src="{}">'.format(url_for('static', filename=img)))
    resp.set_cookie('visited', 'true')
    return resp

@app.route('/ever')
def set_evercookie():
    return ('Not implemented yet', 501)
