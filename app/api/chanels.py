from fastapi import APIRouter
from fastapi import Depends

from app.models.chanels import Chanel
from app.services.chanels import ChanelsService

router = APIRouter(
    prefix='/chanels',
)


@router.get('/',response_model=list[Chanel])
def get_chanels(service: ChanelsService = Depends()):
    return service.get_list()