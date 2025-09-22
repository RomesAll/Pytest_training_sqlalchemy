from candies.repository import CandiesDAO
from candies.schemas import CandyAddSchema, CandySchema

class CandiesService:

    def __init__(self):
        self.candies = CandiesDAO()

    def service_get_candies(self):
        orm = self.candies.dao_get_candies()
        dto = [CandySchema.model_validate(row, from_attributes=True) for row in orm]
        return dto

    def service_get_count_candies(self):
        count = self.candies.dao_get_count_candies()
        return count

    def service_create_candies(self, new_data: list[dict]):
        dto = [CandyAddSchema(**row) for row in new_data]
        res_stmp = self.candies.dao_create_candies(new_data=dto)
        return res_stmp

    def service_delete_candies(self, id: int):
        res_stmp = self.candies.dao_delete_candies(id=id)
        return res_stmp

