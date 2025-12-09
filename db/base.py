from sqlalchemy.orm import declarative_base

Base: type = declarative_base()
"""
SQLAlchemy declarative base class.

All ORM models should inherit from this Base.
"""
