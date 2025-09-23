from candies.service import *
from candies.schemas import CandyAddSchema, CandySchema
from candies.models import Candies
from database import Base, engine, session_maker, settings
import pytest
from sqlalchemy import insert

class TestCandies:
    
    def test_get_candies(self):
        service = CandiesService()
        assert len(service.service_get_candies()) != 0
        assert isinstance(service.service_get_candies()[0], CandySchema)
     
    def test_get_count_candies(self):
        service = CandiesService()
        assert service.service_get_count_candies() == 4
    
    def test_create_candies(self):
        service = CandiesService()
        candies = [
            {'title': 'first'},
            {'title': 'second'},
            {'title': 'another'}
        ]
        assert service.service_create_candies(candies) == 'ok'

    def test_delete_candies(self):
        service = CandiesService()
        assert service.service_delete_candies(2) == 'ok'
