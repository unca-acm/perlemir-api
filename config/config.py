"""
  Author:     Lane Adair (ladair@unca.edu)
  Date:       February 4, 2020
  Version:    0.0.1

  This is the config file for the Perlemir API. Pertinent includes are called
  in this file.
"""

from flask import Flask, request, url_for, session, redirect, escape
from flask_api import status
from flask_json import json_response
from datetime import datetime, timedelta
import bcrypt
import jwt


app = Flask(__name__)
app.secret_key = '#&$*^#YHF#)FH0382'

JWT_SECRET = '#&$*^#YHF#)FH0382'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 20

DEBUG = True
DB = False
DB_HOST = ""
DB_USER = ""
DB_PWD_HASH = ""

if DEBUG:
  print("FINISHED READING CONFIG")
  print(app)