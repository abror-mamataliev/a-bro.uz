from os.path import dirname
from flask import Flask

from src.routes import *
from src.utils.extensions import db
from src.utils.handlers import (
    init_db,
    register_default_routes,
    register_extensions,
    register_template_filters
)


def create_app(state: str = "prod") -> Flask:
    app = Flask(__name__, instance_path=dirname(dirname(__file__)))
    app.config.from_object(f"src.config.{state.capitalize()}Config")

    register_extensions(app)
    register_template_filters(app)
    register_default_routes(app)

    app.register_blueprint(base_router)
    app.register_blueprint(api_router, url_prefix="/api")

    with app.app_context():
        db.create_all()
        init_db()

    return app
