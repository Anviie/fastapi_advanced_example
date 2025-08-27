from fastapi import Query, Body, Path, APIRouter, Depends
from database import async_session_maker
from sqlalchemy import insert, select, func

from models.hotels import HotelsOrm
from shema.hotels_shema import *
from dependencies import PaginationParams
from repositories.hotels import HotelsRepository


# tags используется, что бы переименовать в Документашке название группы ручек.
router = APIRouter(prefix='/hotels', tags=['Отели'])


@router.get('/')
async def get_hotels(field: GetHotel = Depends(), pagination: PaginationParams = Depends()):
    """Получение списка отелей"""
    async with async_session_maker() as session:
        return await HotelsRepository(session=session).get_all(
            id_hotels=field.id,
            location=field.location,
            title=field.location,
            limit=pagination.per_page,
            offset=pagination.page * (pagination.page - 1)
        )


@router.post('/')
async def create_hotel(create_field: PostHotel):
    async with async_session_maker() as session:
        add_hotels_stmt = insert(HotelsOrm).values(**create_field.model_dump())        
        await session.execute(add_hotels_stmt)
        await session.commit()
    return 'Success'

@router.put('/{id}') # Изменение всех параметров за исключение ID (возможно обработать только при предоставлении всех параметров)
def put_hotels(id: int, update_field: Hotel):
    # global hotels
    # for enum, i in enumerate(hotels):
    #     if i['id'] == id:
    #         updated_hotel = {"id": id, **update_field.model_dump()}
    #         hotels[enum] = updated_hotel
    #         return 'Success'
    pass

@router.patch('/{id}')  # Изменение ограниченного кол-ва параметров (>= 1) за исключением ID
def patch_hotels(
    id: int, #  = Path(description='ID')
    update_field: PatchHotel
    ):
    pass
    # global hotels
    # for i in hotels:
    #     if i['id'] == id:
    #         i.update(update_field.model_dump(exclude_unset=True))
    #         return 'Success'

@router.delete('/{hotel_id}')
def delete_hotel(hotel_id: int):
    pass
    #global hotels
    #hotels = [hotel for hotel in hotels if hotel['id'] != hotel_id]
    #return {'status': 'OK'}