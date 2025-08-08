from pydantic import BaseModel, Field

class Hotel(BaseModel):
    id: int | None = None
    title: str | None = None
    name: str | None = None
    page: int | None = Field(1, ge=1)
    per_page: int | None = Field(5, ge=0, le=100)


class PatchHotel(BaseModel):
    title: str | None = Field(None, description='Название Города')
    name: str | None = Field(None)