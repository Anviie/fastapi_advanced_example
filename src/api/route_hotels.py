from fastapi import Query, Body, Path, APIRouter, Depends
from database import async_session_maker
from sqlalchemy import insert, select

from models.hotels import HotelsOrm
from shema.hotels_shema import *
from dependencies import PaginationParams
from docs.docs_api import desc_get_hotels

# tags используется, что бы переименовать в Документашке название группы ручек.
router = APIRouter(prefix='/hotels', tags=['Отели'])


@router.get('/', **desc_get_hotels)
async def get_hotels(field: GetHotel = Depends(), pagination: PaginationParams = Depends()):
    async with async_session_maker() as session:
        query = select(HotelsOrm)
        if field.id: query = query.filter_by(id == field.id)
        if field.title: query = query.filter(HotelsOrm.title.like(f'%{field.title}%'))
        if field.location: query = query.filter(HotelsOrm.location.like(f'%{field.location}%'))
        query = (
            query
            .limit(pagination.per_page)
            .offset(pagination.per_page * (pagination.page - 1))
        )
        result = await session.execute(query)
        
        hotels = result.scalars().all()
        
        # DEBUG SQL
        print(query.compile(compile_kwargs={'literal_binds': True}))
    
    return hotels

@router.post('/')
async def create_hotel(create_field: PostHotel):
    async with async_session_maker() as session:
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