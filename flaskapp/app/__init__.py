from flask import Flask
from flask_jwt_extended import JWTManager
from .routes.main_route import main_route
from .routes.api_route import api_route


app = Flask(__name__)
app.register_blueprint(main_route)
app.register_blueprint(api_route)

app.config["JWT_SECRET_KEY"] = "monggaweb123"
jwt = JWTManager(app)