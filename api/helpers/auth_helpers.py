from datetime import timedelta, datetime
from jose import jwt

from api.config.settings import settings


def create_jwt(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.now() + expires_delta

    to_encode.update({
        'exp': expire,
    })

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

    return encoded_jwt