from fastapi import HTTPException


def check_if_username_exists(username: str):
    if username == 'username2':
        raise HTTPException(
            status_code=400,
            detail='Username already exists',
        )
