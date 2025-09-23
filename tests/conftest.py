import pytest
from database import Base, engine
from config import settings

@pytest.fixture(scope='session', autouse=True)
def setup_db():
    assert settings.DB_MODE == 'TEST'
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)