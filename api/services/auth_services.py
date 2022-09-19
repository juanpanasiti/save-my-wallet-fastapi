from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from datetime import datetime, timedelta
from jose import JWTError, jwt

from api.exceptions.db_exceptions import DuplicateDataError
from api.schemas.login_user_schema import LoginUser
from api.schemas.register_user_schema import RegisterUser
from api.config.settings import settings
from api.database.smw_db import smw_db
from api.database.models import user_model
from api.helpers.auth_helpers import create_jwt


class AuthService:
    def __init__(self, _db_conn=None) -> None:
        self.__db_conn = _db_conn
        self.__pwd_context = None

    @property
    def db_conn(self):
        if self.__db_conn is None:
            # TODO: get conn
            pass
        return self.__db_conn

    @property
    def pwd_context(self):
        if self.__pwd_context is None:
            self.__pwd_context = CryptContext(
                schemes=["bcrypt"], deprecated="auto")
        return self.__pwd_context

    def register_user(self, form: RegisterUser):
        encrypted_password = self.pwd_context.hash(form.password)

        new_user = {
            'username': form.username,
            'email': form.email,
            'password': encrypted_password,
        }
        new_user = user_model.UserModel(**new_user)

        try:
            smw_db.session.add(new_user)
            smw_db.session.commit()
            return True
        except IntegrityError as ie:
            smw_db.session.rollback()
            raise DuplicateDataError(ie.orig.args[1])


    def login_user(self, form: LoginUser):
        user_db = smw_db.session.query(user_model.UserModel).filter(
            user_model.UserModel.username == form.username
        ).first()

        if not user_db:
            # TODO: replace HTTPException here
            raise HTTPException(
                status_code=400,
                detail='Incorrect username/password'
            )

        if not self.pwd_context.verify(form.password, user_db.password):
            # TODO: replace HTTPException here
            raise HTTPException(
                status_code=400,
                detail='Incorrect username/password'
            )

        access_token_expires = timedelta(hours=settings.ACCESS_TOKEN_EXPIRE_HOURS)
        access_token = create_jwt(
            data={'sub': user_db.username},
            expires_delta=access_token_expires
        )
        return {
            'token': access_token
        }