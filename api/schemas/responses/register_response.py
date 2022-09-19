from pydantic import BaseModel

from .base_json_response import ApiJsonResponseBase


class UserProfileDataResponse(BaseModel):
    img_url: str


class UserDataResponse(BaseModel):
    id: int
    username: str
    email: str
    user_profile: UserProfileDataResponse


class RegisterResponseData(BaseModel):
    user_data: UserDataResponse
    token: str
    need_email_confirmation: bool = True


class RegisterResponse(ApiJsonResponseBase):
    response_data: RegisterResponseData
