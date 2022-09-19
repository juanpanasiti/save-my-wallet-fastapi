from pydantic import BaseModel
from typing import Any


class ApiJsonResponseBase(BaseModel):
    response_data: Any