# To import a package in Python, we use the keyword "from" or "import"
from flask import Flask

flask_app = Flask(__name__)

from app import routes

