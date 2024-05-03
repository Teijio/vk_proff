from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDBase:
    def __init__(self, model):
        self.model = model

    async def create(self, obj, session: AsyncSession):
        obj_data = self.model(**obj.model_dump())
        session.add(obj_data)
        await session.commit()
        await session.refresh(obj_data)
        return obj_data

    async def get_by_attribute(self, attr_name: str, attr_value: str, session: AsyncSession):
        attr = getattr(self.model, attr_name)
        db_object = await session.execute(select(self.model).where(attr == attr_value))
        return db_object.scalars().first()

    async def get_multi(self, session: AsyncSession):
        db_objects = await session.execute(select(self.model))
        return db_objects.scalars().all()
