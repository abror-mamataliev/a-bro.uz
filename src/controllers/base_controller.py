from flask import (
    current_app,
    render_template
)

from src.services.base_service import BaseService


class BaseController:

    def __init__(self):
        self.base_service = BaseService()

    def home(self):
        data = self.base_service.get_data()
        return render_template(
            "pages/base.html",
            current_page="home",
            **data
        )

    def about(self):
        data = self.base_service.get_data()
        return render_template(
            "pages/base.html",
            current_page="about",
            **data
        )

    def resume(self):
        data = self.base_service.get_data()
        return render_template(
            "pages/base.html",
            current_page="resume",
            **data
        )

    def services(self):
        data = self.base_service.get_data()
        return render_template(
            "pages/base.html",
            current_page="services",
            **data
        )

    def portfolio(self):
        data = self.base_service.get_data()
        return render_template(
            "pages/base.html",
            current_page="portfolio",
            **data
        )

    def contact(self):
        data = self.base_service.get_data()
        return render_template(
            "pages/base.html",
            current_page="contact",
            **data
        )
