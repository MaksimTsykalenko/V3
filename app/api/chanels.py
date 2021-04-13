from fastapi import APIRouter
from fastapi import Depends

from app.models.chanels import  Chanel, ChanelBase
from app.services.chanels import ChanelsService

router = APIRouter(
    prefix='/chanels',
)


@router.get('/',response_model=list[Chanel])
def get_chanels(service: ChanelsService = Depends()):
    return service.get_list()

@router.post('/',response_model=Chanel)
def create_chanel(
        chanel_data: ChanelBase,
        service: ChanelsService = Depends()
):

    return service.create(chanel_data)