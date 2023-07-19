from flask import Flask


def create_app(state: str = "prod") -> Flask:
    app = Flask(__name__)
    app.config.from_object(f"src.config.{state.capitalize()}Config")
    return app
