from flask import Blueprint

from src.controllers.api_controller import ApiController


api_router = Blueprint("api", __name__)
api_controller = ApiController()

api_router.add_url_rule(
    "/skills/",
    view_func=api_controller.get_skills,
    methods=["GET"]
)
