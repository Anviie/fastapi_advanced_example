from pydantic import BaseModel, Field

class Hotel(BaseModel):
    id: int | None = None
    title: str | None = None
    name: str | None = None
    page: int | None = 1
    per_page: int | None = 5


class PatchHotel(BaseModel):
    title: str | None = Field(None, description='Название Города')
    name: str | None = Field(None)