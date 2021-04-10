from fastapi import APIRouter
from fastapi import Depends
from datetime import datetime
from typing import Optional

from app.models.shows import Show
from app.services.shows import ShowsService

router = APIRouter(
    prefix='/shows',
)

@router.get('/{chanel_id}',response_model=list[Show])
def get_chanels(
        chanel_id: int,
        start_t: Optional[datetime]=None,
        end_t: Optional[datetime]=None,
        service: ShowsService = Depends()):
    return service.get_list(chanel_id, start_t=start_t, end_t=end_t)