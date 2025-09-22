from pydantic import BaseModel, Field
from typing import Optional

class CandyAddSchema(BaseModel):
    title: str = Field(default='Конфета')
    state: str = Field(default='full')
    owner: str = Field(default='teacher')

    def get_dict(self):
        return {
            'title': self.title,
            'state': self.state,
            'owner': self.owner
        }

class CandySchema(CandyAddSchema):
    id: int = Field(ge=1)

    def get_dict(self):
        currend_dict: dict = super().get_dict()
        currend_dict.update(id=self.id)