# app/__init__.py

from flask import Flask, render_template

from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio import start_server, config, platform
import flask

import pandas as pd
import numpy as np
import datetime

import numpy_financial as npf


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():

        return render_template('index.html')


    return app
