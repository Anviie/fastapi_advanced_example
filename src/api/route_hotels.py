from fastapi import Query, Body, Path, APIRouter
from database import async_session_maker
from sqlalchemy import insert

from models.hotels import HotelsOrm
from shema.hotels_shema import *
from docs.example import examples_post
from docs.docs_api import desc

# tags используется, что бы переименовать в Документашке название группы ручек.
router = APIRouter(prefix='/hotels', tags=['Отели'])



@router.get('/', **desc)
def get_hotels(field: GetHotel = Query()):    
    filtred = hotels
    
    if field.id: filtred = [i for i in filtred if i['id'] == field.id]
    if field.title: filtred =  [i for i in filtred if i['title'] == field.title]
    if field.name: filtred = [i for i in filtred if i['name'] == field.name]
    
    filtred = filtred[:field.page*field.per_page]
    
    return filtred

@router.post('/') # Что бы получить данные из тела сообщения, строим из входящей переменной обьект Body / embed - делает из строки json (ключ - переменная / значение input)
async def create_hotel(create_field: PostHotel):
    async with async_session_maker() as session:
        # НА БУДУЩЕЕЕ - ВЛАДИСЛАВ СХЕМА ВЯЖЕТСЯ С МОДЕЛЬЮ В СТРОКЕ НИЖЕ | В инсерте указывается куда я пишу данные!!!!
        add_hotels_stmt = insert(HotelsOrm).values(**create_field.model_dump())
        await session.execute(add_hotels_stmt)
        await session.commit()
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

@router.delete('/{hotel_id}')
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel['id'] != hotel_id]
    return {'status': 'OK'}