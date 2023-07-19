from flask import Flask

from src.routes import *


def create_app(state: str = "prod") -> Flask:
    app = Flask(__name__)
    app.config.from_object(f"src.config.{state.capitalize()}Config")

    app.register_blueprint(base)

    return app
