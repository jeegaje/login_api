from flask import Flask
from flask_jwt_extended.jwt_manager import JWTManager
from flask_cors import CORS

from config import Config
from .routes.api_route import *

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
app.register_blueprint(apiRoute)

jwt = JWTManager(app)