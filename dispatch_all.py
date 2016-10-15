# Runs all of the sites from evil, each with its own URL prefix.
# Will serve your_module at /your_module iff it is imported in evil/__init__.py.

from flask import Flask
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

import evil

# get all "useful things" in evil, and hang them at /name
SITES = {'/'+m: getattr(evil, m).app for m in dir(evil) if not m.startswith('_')}

index_page = Flask(__name__)
@index_page.route('/')
def list_sites():
	return ('<ul>' +
	        ''.join(['<li><a href="{}">{}</a></li>'.format(s, s) for s in SITES]) +
	        '</ul>')

application = DispatcherMiddleware(index_page, SITES)
if __name__ == '__main__':
    run_simple('localhost', 5000, application,
               use_reloader=True, use_debugger=True, use_evalex=True)
