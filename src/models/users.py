from pydantic import BaseModel, EmailStr

from src.models import events


class User(BaseModel):
    email: EmailStr
    password: str
    events: list[events.Event] | None

    class Config:
        schema_extra = {  # noqa: RUF012
            "example": {
                "email": "user@email.com",
                "password": "strong!!",
                "events": [],
            },
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {  # noqa: RUF012
            "example": {
                "email": "user@email.com",
                "password": "strong!!",
                "events": [],
            },
        }
