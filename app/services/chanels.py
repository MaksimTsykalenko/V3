from fastapi import Depends
from sqlalchemy.orm import Session

from app.db import tables
from app.db.database import get_session
from app.models.chanels import ChanelBase

class ChanelsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> list[tables.Chanel]:
        query = self.session.query(tables.Chanel)
        chanels = query.all()
        return chanels

    def create(self, chanel_data: ChanelBase ) -> tables.Chanel:
        chanel = tables.Chanel(**chanel_data.dict())
        self.session.add(chanel)
        self.session.commit()
        return chanel