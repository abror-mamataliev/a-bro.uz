from enum import Enum

from src.utils.extensions import db
from .base import BaseModel, ModelMixin


class Skill(BaseModel):

    name = db.Column(db.String(100), nullable=False)
    percent = db.Column(db.Integer, nullable=False, default=30, index=True)


class Interest(BaseModel):

    name = db.Column(db.String(100), nullable=False)
    icon = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(7), nullable=False)


class Testimonial(BaseModel):

    full_name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)


class ExperienceTypeEnum(Enum):

    EDUCATION = "EDUCATION"
    PROFESSION = "PROFESSION"


class Experience(BaseModel):

    title = db.Column(db.String(100), nullable=False)
    type = db.Column(db.Enum(ExperienceTypeEnum), nullable=False, index=True)
    place = db.Column(db.String(150), nullable=False)
    start_date = db.Column(db.Date, nullable=False, index=True)
    end_date = db.Column(db.Date)


class ExperienceInfo(ModelMixin):

    __tablename__ = "experience_info"

    experience_id = db.Column(
        db.Integer,
        db.ForeignKey("experience.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False
    )
    content = db.Column(db.String, nullable=False)


class Service(BaseModel):

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String)
    icon = db.Column(db.String(50), nullable=False)


class Social(BaseModel):

    name = db.Column(db.String(50), nullable=False)
    icon = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String, nullable=False)


class Project(BaseModel):

    name = db.Column(db.String(80), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date, nullable=False, index=True)
    end_date = db.Column(db.Date)


class ProjectImage(ModelMixin):

    project_id = db.Column(
        db.Integer,
        db.ForeignKey("project.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    image = db.Column(db.String, nullable=False)


class ProjectType(BaseModel):

    __tablename__ = "project_type"

    name = db.Column(db.String(80), nullable=False)


project_types = db.Table(
    "project_types",
    db.Column("id", db.Integer, primary_key=True),
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


class Meta(BaseModel):

    key = db.Column(db.String, nullable=False, index=True)
    value = db.Column(db.String(255))
    type = db.Column(db.String(20))
