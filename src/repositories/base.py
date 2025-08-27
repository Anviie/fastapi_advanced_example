from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase
from typing import ClassVar, Type, Optional

class BaseRepository:
    model: ClassVar[Type[DeclarativeBase]] = None
        
    def __init__(self, session, *args, **kwargs):
        self.session = session        

    async def get_all(self):
        if self.model is None:
            raise NotImplementedError(f'{self.__class__.__name__} must be define "model"')
        query = select(self.model)
        result = await self.session.execute(query)
        
        return result.scalars().all()
    
    async def get_one_or_none(self, **filter_by):
        if self.model is None:
            raise NotImplementedError(f'{self.__class__.__name__} must be define "model"')
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        
        return result.scalars().one_or_none()