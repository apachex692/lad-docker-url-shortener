# Author: Sakthi Santhosh
# Created on: 25/08/2023
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from time import sleep

from lib.config import Config

app_handle = Flask(__name__)
app_handle.config.from_object(Config)

db_handle = SQLAlchemy(app_handle)

import lib.models

from lib.db_init import db_init

db_init()

import lib.routes
