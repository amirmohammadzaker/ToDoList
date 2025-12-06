from sqlalchemy.orm import declarative_base

Base = declarative_base()

from models.project import Project
from models.task import Task
