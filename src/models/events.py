from pydantic import BaseModel


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: list[str]
    location: str

    class Config:
        schema_extra = {  # noqa: RUF012
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyiamge.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to com with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet",
            },
        }
