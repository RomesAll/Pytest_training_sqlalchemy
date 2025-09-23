import pytest
from database import Base, engine

@pytest.fixture(scope='session', autouse=True)
def setup_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)