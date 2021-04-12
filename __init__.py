from Flask_Portfolio.views.portfolio import portfolio
import os
from flask import Flask

app = Flask(__name__)

# setting directory to base path
basedir = os.path.abspath(os.path.dirname(__file__))

# blueprint views
app.register_blueprint(portfolio)
