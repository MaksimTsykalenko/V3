from fastapi import Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.db import tables
from app.db.database import get_session
from app.models.shows import ShowBase


class ShowsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self,
                 chanel_id: int,
                 start_t: datetime,
                 end_t: datetime
                 ) -> list[tables.Chanel]:
        query = self.session.query(tables.Show)
        query = query.filter(tables.Show.c.chanel_id == chanel_id)
        if start_t :
            query = query.filter(tables.Show.c.start_t >= start_t)
        if end_t :
            query = query.filter(tables.Show.c.end_t >= end_t)

        return query.all()

    def create(self, show_data: ShowBase) -> tables.Show:
        show = tables.Show(**show_data.dict())
        self.session.add(show)
        self.session.commit()
        return show
