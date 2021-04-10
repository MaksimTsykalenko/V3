from pydantic import BaseModel
from datetime import datetime


class ShowBase(BaseModel):
    title: str
    description: str
    start_t: datetime
    end_t: datetime
    chanel_id: int

    class Config:
        orm_mode = True

class Show(ShowBase):
    id: str
