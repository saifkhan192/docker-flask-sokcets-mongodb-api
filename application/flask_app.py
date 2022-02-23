import os
import sys

# set /app/application as working dir
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask

app = Flask('Flask App')

app.debug = True if os.environ.get('flask_debug') else False
app.config['SECRET_KEY'] = os.environ.get('FLASK_APP_SECRET_KEY', os.urandom(32))
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['JSON_SORT_KEYS'] = False
