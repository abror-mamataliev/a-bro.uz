from datetime import datetime
from json import load
from flask import (
    Flask,
    current_app,
    redirect,
    send_from_directory,
    url_for
)
from src.models.base import LanguageEnum

from src.models import (
    Experience,
    ExperienceInfo,
    ExperienceTranslation,
    Interest,
    InterestTranslation,
    Project,
    ProjectTranslation,
    ProjectType,
    Service,
    ServiceTranslation,
    Skill,
    Social
)

from .extensions import db


def init_db():
    languages = [
        LanguageEnum.EN,
        LanguageEnum.RU,
        LanguageEnum.UZ
    ]
    with open("data/skills.json", encoding="utf-8") as file:
        skills = load(file)
    for skill in skills:
        skill_entity = Skill.query.filter_by(name=skill['name']).first()
        if skill_entity is None:
            skill_entity = Skill(
                name=skill['name'],
                percent=skill['percent']
            )
            skill_entity.save()
    with open("data/interests.json", encoding="utf-8") as file:
        interests = load(file)
    for interest in interests:
        interest_entity = Interest.query. \
            join(InterestTranslation, InterestTranslation.interest_id == Interest.id) \
            .filter(
                InterestTranslation.name == interest['name']['en'],
                InterestTranslation.language == LanguageEnum.EN
            ).first()
        if interest_entity is None:
            interest_entity = Interest(
                icon=interest['icon'],
                color=interest['color']
            )
            interest_entity.save()
        for language in languages:
            interest_translation = InterestTranslation.query.filter(
                InterestTranslation.interest_id == interest_entity.id,
                InterestTranslation.language == language
            ).first()
            if interest_translation is None:
                interest_translation = InterestTranslation(
                    interest_id=interest_entity.id,
                    name=interest['name'][language.value.lower()],
                    language=language
                )
                interest_translation.save()
    with open("data/socials.json", encoding="utf-8") as file:
        socials = load(file)
    for social in socials:
        social_entity = Social.query.filter_by(name=social['name']).first()
        if social_entity is None:
            social_entity = Social(
                name=social['name'],
                icon=social['icon'],
                url=social['url']
            )
            social_entity.save()
    with open("data/experiences.json", encoding="utf-8") as file:
        experiences = load(file)
    for experience in experiences:
        experience_entity = Experience.query \
            .join(
                ExperienceTranslation,
                ExperienceTranslation.experience_id == Experience.id
            ) \
            .filter(
                ExperienceTranslation.title == experience['title']['en'],
                ExperienceTranslation.language == LanguageEnum.EN,
                Experience.type == experience['type']
            ).first()
        if experience_entity is None:
            experience_entity = Experience(
                type=experience['type'],
                start_date=datetime.strptime(
                    experience['start_date'],
                    "%Y-%m-%d"
                ).date(),
                end_date=datetime.strptime(
                    experience['end_date'],
                    "%Y-%m-%d"
                ).date() if 'end_date' in experience else None
            )
            experience_entity.save()
        for language in languages:
            experience_translation = ExperienceTranslation.query.filter(
                ExperienceTranslation.experience_id == experience_entity.id,
                ExperienceTranslation.language == language
            ).first()
            if experience_translation is None:
                experience_translation = ExperienceTranslation(
                    experience_id=experience_entity.id,
                    title=experience['title'][language.value.lower()],
                    place=experience['place'][language.value.lower()],
                    language=language
                )
                experience_translation.save()
        if 'info' in experience:
            for language in languages:
                for content in experience['info'][language.value.lower()]:
                    experience_info = ExperienceInfo.query.filter_by(
                        experience_id=experience_entity.id,
                        content=content,
                        language=language
                    ).first()
                    if experience_info is None:
                        experience_info = ExperienceInfo(
                            experience_id=experience_entity.id,
                            content=content,
                            language=language
                        )
                        experience_info.save()
    with open("data/services.json", encoding="utf-8") as file:
        services = load(file)
    for service in services:
        service_entity = Service.query. \
            join(ServiceTranslation, ServiceTranslation.service_id == Service.id) \
            .filter(
                ServiceTranslation.name == service['name']['en'],
                ServiceTranslation.language == LanguageEnum.EN
            ).first()
        if service_entity is None:
            service_entity = Service(icon=service['icon'])
            service_entity.save()
        for language in languages:
            service_translation = ServiceTranslation.query.filter(
                ServiceTranslation.service_id == service_entity.id,
                ServiceTranslation.language == language
            ).first()
            if service_translation is None:
                service_translation = ServiceTranslation(
                    service_id=service_entity.id,
                    name=service['name'][language.value.lower()],
                    description=service['description'][language.value.lower()],
                    language=language
                )
                service_translation.save()
    with open("data/projects.json", encoding="utf-8") as file:
        projects = load(file)
    for project in projects:
        project_entity = Project.query. \
            join(ProjectTranslation, ProjectTranslation.project_id == Project.id) \
            .filter(
                ProjectTranslation.name == project['name']['en'],
                ProjectTranslation.language == LanguageEnum.EN
            ).first()
        if project_entity is None:
            project_entity = Project(
                url=project['url'],
                image=project['image'],
                client=project['client'],
                date=datetime.strptime(project['date'], "%d-%m-%Y")
            )
            project_entity.save()
        for project_type in project['types']:
            project_type_entity = ProjectType.query.filter(
                ProjectType.name == project_type
            ).first()
            if project_type_entity is None:
                project_type_entity = ProjectType(name=project_type)
                project_type_entity.save()
            if len(list(filter(
                lambda t: t.id == project_type_entity.id,
                project_entity.types
            ))) == 0:
                project_entity.types.append(project_type_entity)
        project_entity.save()
        for language in languages:
            project_translation = ProjectTranslation.query.filter(
                ProjectTranslation.project_id == project_entity.id,
                ProjectTranslation.language == language
            ).first()
            if project_translation is None:
                project_translation = ProjectTranslation(
                    project_id=project_entity.id,
                    name=project['name'][language.value.lower()],
                    description=project['description'][language.value.lower()],
                    language=language
                )
                project_translation.save()


def register_extensions(app: Flask) -> None:
    db.init_app(app)


def register_default_routes(app: Flask) -> None:
    @app.route("/favicon.ico", methods=["GET"])
    def favicon():
        return redirect(url_for("static", filename="icons/favicon.ico"))
    
    @app.route("/uploads/<path:path>", methods=["GET"])
    def uploads(path):
        return send_from_directory(current_app.config['UPLOADS_FOLDER'], path)


def register_template_filters(app: Flask) -> None:
    @app.template_filter("form_datetime")
    def form_datetime(string: str, format: str) -> datetime:
        return datetime.strptime(string, format)
    
    @app.template_filter("format_datetime")
    def format_datetime(date_time: datetime, format: str) -> str:
        return date_time.strftime(format)
    
    @app.template_filter("get_years_from_today")
    def get_years_from_today(date_time: datetime):
        return (datetime.now() - date_time).days // 365
