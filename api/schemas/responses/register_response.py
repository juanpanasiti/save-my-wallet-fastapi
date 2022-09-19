from pydantic import BaseModel

from .base_json_response import ApiJsonResponseBase


class RegisterResponseData(BaseModel):
    token: str
    need_email_confirmation: bool = True


class RegisterResponse(ApiJsonResponseBase):
    response_data: RegisterResponseData
