from pydantic import BaseModel
from typing import Any

from api.validations import db_validations


class LoginUser(BaseModel):
    username: str
    # email: str
    password: str

    class Config:
        schema_extra = {
            'example': {
                'username': 'johndoe.89',
                # 'email': 'john.doe@fakemail.com',
                'password': 'secret_password',
            }
        }