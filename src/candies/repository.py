from candies.models import Candies
from database import session_maker
from sqlalchemy import Integer, select, insert, delete, func

class CandiesDAO:

    def dao_get_candies(self):
        with session_maker() as session:
            query = select(Candies)
            res_query = session.execute(query)
            return res_query.scalars().all()
    
    def dao_get_count_candies(self):
        with session_maker() as session:
            query = select(func.count().cast(Integer).label('count_candies')).select_from(Candies)
            res_query = session.execute(query)
            return res_query.all()[0][0]
    
    def dao_create_candies(self, new_data: list[dict]):
        result = None
        with session_maker() as session:
            stmt = insert(Candies).values(new_data)
            res_query = session.execute(stmt)
            session.commit()
        return result
    
    def dao_delete_candies(self, id: int):
        result = None
        with session_maker() as session:
            query = delete(Candies).where(Candies.id == id)
            res_query = session.execute(query)
            session.commit()
            
        return result
