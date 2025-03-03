"""Notes"""

from sqlite_database import BaseModel, model, Primary
from database import db

@model(db)
class Notes(BaseModel):
    """Notes Model"""
    __schema__ = (Primary('id'),)

    id: str
    title: str
    content: str
