from repositories.base import BaseRepository
from models.hotels import HotelsOrm
from sqlalchemy import select

class HotelsRepository(BaseRepository):
    model = HotelsOrm
    
    async def get_all(
        self,
        id_hotels,
        location,
        title,
        limit,
        offset
    ):
        query = select(HotelsOrm)
        if id_hotels: query = query.filter(HotelsOrm.id == id_hotels)
        if title: query = query.filter(HotelsOrm.title.like(f'%{title.lower()}%'))
        
        # Вариант через метод contains - упрощенная реализация like, без построения строки
        if location: query = query.filter(HotelsOrm.location.contains(location.lower()))
        
        query = (
            query
            .limit(limit)
            .offset(offset)
        )
        result = await self.session.execute(query)
        return result.scalars().all()
        # DEBUG SQL
        # print(query.compile(compile_kwargs={'literal_binds': True}))
        
    async def post_data(self):
        pass