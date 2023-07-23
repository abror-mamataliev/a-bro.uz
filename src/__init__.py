from os.path import dirname
from flask import Flask

from src.routes import *
from src.utils.extensions import db
from src.utils.handlers import (
    init_db,
    register_extensions
)


def create_app(state: str = "prod") -> Flask:
    app = Flask(__name__, instance_path=dirname(dirname(__file__)))
    app.config.from_object(f"src.config.{state.capitalize()}Config")

    register_extensions(app)

    app.register_blueprint(base_router)

    with app.app_context():
        db.create_all()
        init_db()

    return app
