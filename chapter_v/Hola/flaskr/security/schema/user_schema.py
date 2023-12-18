from pydantic import BaseModel, EmailStr, field_validator
from pydantic_core import PydanticCustomError
from flaskr.utils.password import validate


class UserBody(BaseModel):
    username: str
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
