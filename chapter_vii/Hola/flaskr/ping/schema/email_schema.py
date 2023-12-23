# -*- coding: utf-8 -*-
from pydantic import BaseModel, EmailStr


class RecipientBody(BaseModel):
    name: str
    email: EmailStr
