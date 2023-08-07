from flask import Blueprint

from src.controllers.base_controller import BaseController


base_router = Blueprint("base", __name__)
base_controller = BaseController()

base_router.add_url_rule(
    "/",
    view_func=base_controller.home,
    methods=["GET"]
)
base_router.add_url_rule(
    "/about/",
    view_func=base_controller.about,
    methods=["GET"]
)
base_router.add_url_rule(
    "/resume/",
    view_func=base_controller.resume,
    methods=["GET"]
)
base_router.add_url_rule(
    "/services/",
    view_func=base_controller.services,
    methods=["GET"]
)
base_router.add_url_rule(
    "/portfolio/",
    view_func=base_controller.portfolio,
    methods=["GET"]
)
base_router.add_url_rule(
    "/portfolio/<int:id>/",
    view_func=base_controller.project,
    methods=["GET"]
)
base_router.add_url_rule(
    "/contact/",
    view_func=base_controller.contact,
    methods=["GET", "POST"]
)
