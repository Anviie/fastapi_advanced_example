from fastapi import Query, Body, Path, APIRouter
from pydantic import BaseModel

# tags используется, что бы переименовать в Документашке название группы ручек.
router = APIRouter(prefix='/hotels', tags=['Отели'])


class Hotel(BaseModel):
    tile: str
    name: str


class PatchHotel(BaseModel):
    title: str | None = None
    name: str | None = None


# Псевдо данные из БД
hotels = [
    {'id': 1, 'title': 'Sochi', 'name': 'voc'},
    {'id': 2, 'title': 'Dubai', 'name': 'bok'},
]


@router.get('/')
def get_hotels(
    id: int | None = Query(None, description='Уникальный идентификатор'),
    title: str | None = Query(None, description='Название отеля'),
):
    if id == None or title == None: return hotels # All return
    return [hotel for hotel in hotels if hotel['title'] == title and hotel['id'] == id] # returns the result with the condition

@router.delete('/{hotel_id}')
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel['id'] != hotel_id]
    return {'status': 'OK'}

@router.post('/') # Что бы получить данные из тела сообщения, строим из входящей переменной обьект Body / embed - делает из строки json (ключ - переменная / значение input)
def create_hotel(create_field: Hotel):
    global hotels
    id_max = max([i['id'] for i in hotels]) + 1
    hotel_dict = {'id': id_max, **create_field.model_dump()}
    hotels.routerend(hotel_dict)
    return 'Success'

@router.put('/{id}') # Изменение всех параметров за исключение ID (возможно обработать только при предоставлении всех параметров)
def put_hotels(id: int, update_field: Hotel = Body()):
    global hotels
    for enum, i in enumerate(hotels):
        if i['id'] == id:
            updated_hotel = {"id": id, **update_field.model_dump()}
            hotels[enum] = updated_hotel
            return 'Success'

@router.patch('/{id}')  # Изменение ограниченного кол-ва параметров (>= 1) за исключением ID
def patch_hotels(
    id: int = Path(description='ID'),
    update_field: PatchHotel = Body()
    ):
    global hotels
    for i in hotels:
        if i['id'] == id:
            i.update(update_field.model_dump(exclude_unset=True))
            return 'Success'
