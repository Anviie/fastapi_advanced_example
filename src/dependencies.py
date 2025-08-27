from pydantic import BaseModel, Field

class PaginationParams(BaseModel):
    page: int = Field(1, ge=1)
    per_page: int = Field(5, ge=0, le=100)