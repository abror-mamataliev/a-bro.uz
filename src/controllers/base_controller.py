from flask import render_template
from src.services.base_service import BaseService


class BaseController:

    def __init__(self):
        self.base_service = BaseService()

    def home(self):
        return render_template("pages/base/home.html")
