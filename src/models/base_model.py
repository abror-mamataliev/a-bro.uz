from enum import Enum

from src.utils.extensions import db
from .base import (
    BaseModel,
    TranslationModel
)


class Skill(BaseModel):

    name = db.Column(db.String(100), nullable=False)
    percent = db.Column(db.Integer, nullable=False, default=30, index=True)

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'percent': self.percent
        }


class Interest(BaseModel):

    icon = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(7), nullable=False)

    def name(self, language: str) -> str:
        interest_translation = InterestTranslation.query.filter(
            InterestTranslation.interest_id == self.id,
            InterestTranslation.language == language.upper()
        ).first()
        return interest_translation.name if interest_translation is not None else ""


class InterestTranslation(TranslationModel):

    __tablename__ = "interest_translation"

    interest_id = db.Column(
        db.Integer,
        db.ForeignKey("interest.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    name = db.Column(db.String(100), nullable=False)


class Testimonial(TranslationModel):

    full_name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)


class ExperienceTypeEnum(Enum):

    EDUCATION = "EDUCATION"
    PROFESSION = "PROFESSION"


class Experience(BaseModel):

    type = db.Column(db.Enum(ExperienceTypeEnum), nullable=False, index=True)
    start_date = db.Column(db.Date, nullable=False, index=True)
    end_date = db.Column(db.Date)

    info = db.relationship("ExperienceInfo", backref="experience", lazy=True)

    def title(self, language: str) -> str:
        experience_translation = ExperienceTranslation.query.filter(
            ExperienceTranslation.experience_id == self.id,
            ExperienceTranslation.language == language.upper()
        ).first()
        return experience_translation.title if experience_translation is not None else ""

    def place(self, language: str) -> str:
        experience_translation = ExperienceTranslation.query.filter(
            ExperienceTranslation.experience_id == self.id,
            ExperienceTranslation.language == language.upper()
        ).first()
        return experience_translation.place if experience_translation is not None else ""


class ExperienceTranslation(TranslationModel):

    __tablename__ = "experience_translation"

    experience_id = db.Column(
        db.Integer,
        db.ForeignKey("experience.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    title = db.Column(db.String(100), nullable=False)
    place = db.Column(db.String(150), nullable=False)


class ExperienceInfo(TranslationModel):

    __tablename__ = "experience_info"

    experience_id = db.Column(
        db.Integer,
        db.ForeignKey("experience.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False
    )
    content = db.Column(db.String, nullable=False)


class Service(BaseModel):

    icon = db.Column(db.String(50), nullable=False)

    def name(self, language: str) -> str:
        service_translation = ServiceTranslation.query.filter(
            ServiceTranslation.service_id == self.id,
            ServiceTranslation.language == language.upper()
        ).first()
        return service_translation.name if service_translation is not None else ""

    def description(self, language: str) -> str:
        service_translation = ServiceTranslation.query.filter(
            ServiceTranslation.service_id == self.id,
            ServiceTranslation.language == language.upper()
        ).first()
        return service_translation.description if service_translation is not None else ""


class ServiceTranslation(TranslationModel):

    __tablename__ = "service_translation"

    service_id = db.Column(
        db.Integer,
        db.ForeignKey("service.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String)


class Social(BaseModel):

    name = db.Column(db.String(50), nullable=False)
    icon = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String, nullable=False)


project_types = db.Table(
    "project_types",
    db.Column(
        "project_id",
        db.Integer,
        db.ForeignKey("project.id", ondelete="CASCADE", onupdate="CASCADE")
    ),
    db.Column(
        "project_type_id",
        db.Integer,
        db.ForeignKey("project_type.id", ondelete="CASCADE", onupdate="CASCADE")
    )
)


class Project(BaseModel):

    url = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String, nullable=False)
    client = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False, index=True)

    types = db.relationship("ProjectType", secondary=project_types, backref="projects")

    def name(self, language: str) -> str:
        project_translation = ProjectTranslation.query.filter(
            ProjectTranslation.project_id == self.id,
            ProjectTranslation.language == language.upper()
        ).first()
        return project_translation.name if project_translation is not None else ""

    def description(self, language: str) -> str:
        project_translation = ProjectTranslation.query.filter(
            ProjectTranslation.project_id == self.id,
            ProjectTranslation.language == language.upper()
        ).first()
        return project_translation.description if project_translation is not None else ""


class ProjectTranslation(TranslationModel):

    __tablename__ = "project_translation"

    project_id = db.Column(
        db.Integer,
        db.ForeignKey("project.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)


class ProjectType(BaseModel):

    __tablename__ = "project_type"

    name = db.Column(db.String(80), nullable=False)
