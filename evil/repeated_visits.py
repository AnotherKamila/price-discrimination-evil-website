"""Returns a different response based on whether this site was visited before.

Uses a simple cookie.
"""

from flask import Flask, make_response, request, url_for
app = Flask(__name__)

@app.route('/')
def simple_cookie():
    if 'visited' not in request.cookies:
        data, img = 42, '1.jpg'
    else:
        data, img = 47, '2.jpg'

    resp = make_response('<img src="{}"><p>Data: <b class="data">{}</b></p>'.format(
        url_for('static', filename=img), data))
    resp.set_cookie('visited', 'true')
    return resp

@app.route('/ever')
def set_evercookie():
    return ('Not implemented yet', 501)
