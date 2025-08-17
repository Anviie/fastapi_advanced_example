from pydantic import BaseModel, Field

class PaginationParams(BaseModel):
    page: int | None = Field(1, ge=1)
    per_page: int | None = Field(5, ge=0, le=100)