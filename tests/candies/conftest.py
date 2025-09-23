import pytest
from sqlalchemy import insert
from candies.models import Candies
from database import Base, engine, session_maker, settings

@pytest.fixture(scope='class', autouse=True)
def default_data_for_db():
    with session_maker() as session:
        candies = [
            {'title': 'candie1'},
            {'title': 'candie2'},
            {'title': 'candie3'},
            {'title': 'candie4'}
        ]

        stmt = insert(Candies).values(candies)
        res = session.execute(stmt)
        session.commit()