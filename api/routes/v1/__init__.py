from fastapi import APIRouter

from .auth_routes import auth_router


router_v1 = APIRouter(prefix='/v1', tags=['Version 1'])

router_v1.include_router(auth_router)

