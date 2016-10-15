"""Runs all of the sites from evil, each with its own URL prefix.

Will serve your_module at /your_module iff it is imported in evil/__init__.py
and exports `app`, which is a Flask application.

Also generates a nice index of all known sites.
"""

from flask import Flask
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

import evil

# get all "useful things" in evil, and hang them at /name
SITES = {'/'+m: getattr(evil, m) for m in dir(evil) if not m.startswith('_')}

index_page = Flask(__name__)
@index_page.route('/')
def list_sites():
    def li(s):
        return '<li><a href="{}">{}</a>: {}</li>'.format(s, s, SITES[s].__doc__)
    return '<ul>' + ''.join([li(s) for s in sorted(SITES)]) + '</ul>'

application = DispatcherMiddleware(index_page, {s: SITES[s].app for s in SITES})
if __name__ == '__main__':
    run_simple('localhost', 5000, application,
               use_reloader=True, use_debugger=True, use_evalex=True)
