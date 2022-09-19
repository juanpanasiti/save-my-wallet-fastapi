from pydantic import BaseModel
from typing import Any

from api.validations import db_validations


class RegisterUser(BaseModel):
    def __init__(__pydantic_self__, **data: Any) -> None:
        db_validations.check_if_username_exists(data['username'])
        super().__init__(**data)

    username: str
    email: str
    password: str

    class Config:
        schema_extra = {
            'example': {
                'username': 'johndoe.89',
                'email': 'john.doe@fakemail.com',
                'password': 'secret_password',
            }
        }
