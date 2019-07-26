from flask import Flask

app = Flask(__name__)

from app.routes import app
from flask import render_template
