from fastapi import APIRouter, HTTPException

from api.schemas.register_user_schema import RegisterUser
from api.exceptions.db_exceptions import DuplicateDataError
from api.schemas.login_user_schema import LoginUser
from api.schemas.responses.register_response import RegisterResponse
from api.services.auth_services import AuthService

auth_router = APIRouter(prefix='/auth', tags=['Auth', 'Users'])
auth_services = AuthService()


@auth_router.post('/sign_up', response_model=RegisterResponse)
async def sign_up(form: RegisterUser):
    try:
        new_user = auth_services.register_user(form)
    except DuplicateDataError as dde:
        raise HTTPException(
            status_code=400,
            detail=dde.msg
        )
    return {
        'response_data': {
            'new_user': new_user,
            'token': 'asdfsadfsdf',
            'need_email_confirmation': False
        }
    }


@auth_router.post('/sign_in')
async def sign_in(form: LoginUser):
    token = auth_services.login_user(form)
    return token
