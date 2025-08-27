from pydantic import BaseModel, Field
from fastapi import Query


class Hotel(BaseModel):
    id: int | None = None
    title: str | None = None
    location: str | None = None    


class PostHotel(BaseModel):
    title: str = Field(
        description="Официальное название отеля. Максимум 50 символов.",
        title="Название",
        example="Olem",
        max_length=50,
    ) # pyright: ignore[reportCallIssue]
    location: str = Field(
        description="Город, улица, район. Максимум 100 символов.",
        title="Адрес или локация",
        example="Dubai, street 1",
        max_length=100,
    ) # pyright: ignore[reportCallIssue]

class GetHotel(BaseModel):
    id: int | None = Query(None, description='Айдишка')
    title: str | None = Query(None, description='Название отеля')
    location: str | None = Query(None, description='Адрес')


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