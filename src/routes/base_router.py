from flask import Blueprint

from src.controllers.base_controller import BaseController


base = Blueprint("base", __name__)
base_controller = BaseController()

@base.route('/', methods=["GET"])
def home():
    return base_controller.home()
