from fastapi import APIRouter

from .chanels import router as chanels_router
from .shows import router as shows_router

router = APIRouter()
router.include_router(chanels_router)
router.include_router(shows_router)