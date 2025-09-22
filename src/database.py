
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from sqlalchemy import MetaData, create_engine
from config import settings

engine = create_engine(
    url=settings.DATABASE_URL_sync,
    echo=True
)

class Base(DeclarativeBase):
    metadata = MetaData()

session_maker = sessionmaker(engine)