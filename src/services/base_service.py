from flask import current_app

from src.models.base_model import (
    Interest,
    Skill,
    Social
)


class BaseService:

    def get_data(self):
        base_url = current_app.config.get('BASE_URL')
        skills = Skill.query.all()
        interests = Interest.query.all()
        socials = Social.query.all()
        return {
            'base_url': base_url,
            'skills': skills,
            'interests': interests,
            'socials': socials
        }
