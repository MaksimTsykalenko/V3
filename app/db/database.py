from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.setting import settings


database_url = settings.database_url
engine = create_engine(database_url)

Session = sessionmaker(engine)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()