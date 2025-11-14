"""Notes"""

from luminadb import BaseModel, model, Primary
from database import db

@model(db)
class Notes(BaseModel):
    """Notes Model"""
    __schema__ = (Primary('id'),)

    id: str
    title: str
    content: str
    created_at: float
    modified_at: float = 0
