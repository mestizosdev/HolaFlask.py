from pydantic import BaseModel, EmailStr, field_validator, constr
from pydantic_core import PydanticCustomError
from typing import Optional
from flaskr.utils.password import validate


class UserBody(BaseModel):
    username: constr(min_length=3, max_length=18, pattern=r'^[A-Za-z0-9_-]+$')
    email: EmailStr
    password: str

    @field_validator('password')
    def check_password(cls, value: str) -> str:
        is_valid, message = validate(value)
        if not is_valid:
            raise PydanticCustomError(
                'value_error',
                message,
                dict(reason='Not valid password'),
            )
        return value


class UserBodyLogin(UserBody):
    email: Optional[EmailStr] = None


class UserBodyUpdate(UserBody):
    password: Optional[str] = None
    status: bool
