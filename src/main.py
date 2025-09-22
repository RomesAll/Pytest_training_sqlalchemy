from database import *
from config import *
from sqlalchemy import Integer, func, select, text
from candies.models import *
from candies.service import *


s = CandiesService()
s.service_create_candies([{'title': 'aboba'}, {'title': 'vcvv'}])