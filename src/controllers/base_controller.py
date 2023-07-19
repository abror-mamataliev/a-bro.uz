from src.services.base_service import BaseService


class BaseController:

    def __init__(self):
        self.base_service = BaseService()

    def index(self):
        return self.base_service.home()
