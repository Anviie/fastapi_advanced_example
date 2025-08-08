from fastapi import Query, Body, Path, APIRouter
from shema.hotels_shema import Hotel, PatchHotel

# tags используется, что бы переименовать в Документашке название группы ручек.
router = APIRouter(prefix='/hotels', tags=['Отели'])


# Псевдо данные из БД
hotels = [
    {"id": 1, "title": "Sochi", "name": "sochi"},
    {"id": 2, "title": "Дубай", "name": "dubai"},
    {"id": 3, "title": "Мальдивы", "name": "maldivi"},
    {"id": 4, "title": "Геленджик", "name": "gelendzhik"},
    {"id": 5, "title": "Москва", "name": "moscow"},
    {"id": 6, "title": "Казань", "name": "kazan"},
    {"id": 7, "title": "Санкт-Петербург", "name": "spb"},
]


@router.get('/')
def get_hotels(
    field: Hotel = Query()
):    
    filtred = hotels
    
    if field.id: filtred = [i for i in filtred if i['id'] == field.id]
    if field.title: filtred =  [i for i in filtred if i['title'] == field.title]
    if field.name: filtred = [i for i in filtred if i['name'] == field.name]
    
    filtred = filtred[:field.page*field.per_page]
    
    return filtred

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
def put_hotels(id: int, update_field: Hotel):
    global hotels
    for enum, i in enumerate(hotels):
        if i['id'] == id:
            updated_hotel = {"id": id, **update_field.model_dump()}
            hotels[enum] = updated_hotel
            return 'Success'

@router.patch('/{id}')  # Изменение ограниченного кол-ва параметров (>= 1) за исключением ID
def patch_hotels(
    id: int, #  = Path(description='ID')
    update_field: PatchHotel
    ):
    global hotels
    for i in hotels:
        if i['id'] == id:
            i.update(update_field.model_dump(exclude_unset=True))
            return 'Success'
