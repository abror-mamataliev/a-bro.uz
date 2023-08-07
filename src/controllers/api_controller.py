from flask import jsonify

from src.services.base_service import BaseService


class ApiController:

    def __init__(self):
        self.base_service = BaseService()
    
    def get_skills(self):
        return jsonify(self.base_service.get_skills())
