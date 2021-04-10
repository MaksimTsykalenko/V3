from pydantic import BaseModel
from typing import Optional


class ChanelBase(BaseModel):
    title: Optional[str]
    icon: Optional[str]
    disabled: bool = False

    class Config:
        orm_mode = True


class Chanel(ChanelBase):
    id: int
