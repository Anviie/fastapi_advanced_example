from typing import TypedDict
from fastapi import APIRouter, Depends, Response

class RouteInfo(TypedDict, total=False):
    summary: str
    description: str
    response_description: str
    tags: list[str]
    deprecated: bool
    status_code: int
    # ... и другие, если нужно

desc_get_hotels: RouteInfo = {
    "summary": "Получение списка отелей",
    "description": "Получение списка отелей",
    "response_description": "Возвращает отели по выбранным параметрам",
}