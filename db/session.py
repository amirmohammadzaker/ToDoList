import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

# Load environment variables from .env file
load_dotenv()

DATABASE_URL: str | None = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    echo=False
)

SessionLocal: sessionmaker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_session() -> Generator[Session, None, None]:
    """
    Provide a SQLAlchemy session generator for dependency injection.

    Yields:
        SQLAlchemy Session instance.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
