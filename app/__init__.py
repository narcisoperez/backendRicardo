from flask import Flask
from app.extensions import db
from app.routes.auth import auth_bp
from app.config import Config
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    JWTManager(app)

    app.register_blueprint(auth_bp)

    return app
