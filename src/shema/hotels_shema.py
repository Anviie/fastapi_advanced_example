from pydantic import BaseModel, Field

class Hotel(BaseModel):
    id: int | None = None
    title: str | None = None
    location: str | None = None    


class PostHotel(BaseModel):
    title: str = Field(
        description='Название Отеля',
        title="Название",
        example='Olem',
        max_length=50,
    )
    location: str = Field(
        description='Географическое положение',
        title="Название",
        example='Dubaui, street 1',
        max_length=100,
    )

class GetHotel(BaseModel):
    id: int | None = None
    title: str | None = None
    location: str | None = None
    page: int | None = Field(1, ge=1)
    per_page: int | None = Field(5, ge=0, le=100)


class PatchHotel(BaseModel):
    title: str | None = Field(None, description='Название Города')
    location: str | None = Field(None)
    
# class Item(BaseModel):
#     name: str = Field(
#         ...,  # обязательное поле (аналог Required)
#         description="Название товара",
#         example="Ноутбук",
#         min_length=2,
#         max_length=100,
#         pattern=r"^[a-zA-Z0-9\s]+$",
#         title="Название",
#     )
#     price: float = Field(
#         ...,
#         gt=0,  # > 0
#         le=10000,  # <= 10000
#         description="Цена в долларах",
#         example=999.99,
#     )
#     quantity: int = Field(
#         default=1,
#         ge=0,  # >= 0
#         description="Количество на складе",
#         example=50
#     )
#     category: str = Field(
#         default=None,
#         description="Категория товара",
#         enum=["Electronics", "Books", "Clothing"],  # ограничение значений
#     )