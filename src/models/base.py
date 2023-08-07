from datetime import datetime
from enum import Enum

from src.utils.extensions import db


class ModelMixin(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    def save(self):
        db.session.add(self)
        db.session.commit()


class BaseModel(ModelMixin):

    __abstract__ = True

    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class LanguageEnum(Enum):

    EN = "EN"
    RU = "RU"
    UZ = "UZ"
    FR = "FR"
    TR = "TR"


class TranslationModel(BaseModel):

    __abstract__ = True

    language = db.Column(db.Enum(LanguageEnum))
