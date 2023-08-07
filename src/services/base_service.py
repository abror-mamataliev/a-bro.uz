from flask import current_app
from sqlalchemy import desc

from src.models import (
    Experience,
    ExperienceTypeEnum,
    Interest,
    Project,
    ProjectType,
    Service,
    Skill,
    Social
)


class BaseService:

    def get_data(self):
        base_url = current_app.config.get('BASE_URL')
        skills = Skill.query.all()
        interests = Interest.query.all()
        socials = Social.query.all()
        education = Experience.query.filter_by(
            type=ExperienceTypeEnum.EDUCATION
        ).order_by(desc(Experience.start_date)).all()
        profession = Experience.query.filter_by(
            type=ExperienceTypeEnum.PROFESSION
        ).order_by(desc(Experience.start_date)).all()
        services = Service.query.all()
        projects = Project.query.order_by(desc(Project.date)).all()
        project_types = ProjectType.query.all()
        return {
            'base_url': base_url,
            'skills': skills,
            'interests': interests,
            'socials': socials,
            'education': education,
            'profession': profession,
            'services': services,
            'projects': projects,
            'project_types': project_types
        }
    
    def get_skills(self) -> list[dict]:
        return [skill.format() for skill in Skill.query.all()]
    
    def get_project(self, id: int) -> Project:
        return Project.query.get(id)
    
    def get_project_types_by_id(self, id: int) -> list[str]:
        return [project_type.name for project_type in Project.query.get(id).types]
