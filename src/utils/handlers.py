from json import load
from flask import Flask

from src.models.base_model import (
    Interest,
    Skill,
    Social
)

from .extensions import db


def init_db():
    pass
    # with open("data/skills.json", encoding="utf-8") as file:
    #     skills = load(file)
    # for skill in skills:
    #     skill_entity = Skill.query.filter_by(name=skill['name']).first()
    #     if skill_entity is None:
    #         skill_entity = Skill(
    #             name=skill['name'],
    #             percent=skill['percent']
    #         )
    #         skill_entity.save()
    # with open("data/interests.json", encoding="utf-8") as file:
    #     interests = load(file)
    # for interest in interests:
    #     interest_entity = Interest.query.filter_by(name=interest['name']).first()
    #     if interest_entity is None:
    #         interest_entity = Interest(
    #             name=interest['name'],
    #             icon=interest['icon'],
    #             color=interest['color']
    #         )
    #         interest_entity.save()
    # with open("data/socials.json", encoding="utf-8") as file:
    #     socials = load(file)
    # for social in socials:
    #     social_entity = Social.query.filter_by(name=social['name']).first()
    #     if social_entity is None:
    #         social_entity = Social(
    #             name=social['name'],
    #             icon=social['icon'],
    #             url=social['url']
    #         )
    #         social_entity.save()


def register_extensions(app: Flask) -> None:
    db.init_app(app)
