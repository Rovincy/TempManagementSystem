#!/usr/bin/env python3

from flask import Flask, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

app = Flask(__name__)
api = Api(app)
CORS(app)
load_dotenv()  # take environment variables from .env.
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)
