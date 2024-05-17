
from sqlalchemy import select

from database import new_session
from schemas import STaskAdd, STask
from models import Task


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd):
        async with new_session() as session:
            task_dict = data.model_dump()

            task = Task(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_all(cls)-> list[STask]:
        async with new_session() as session:
            query = select(Task)
            result = await session.execute(query)
            tasks_models = result.scalars().all()
            task_schemas = [STask.model_validate(tasks_models) for tasks_models in tasks_models ]
            return task_schemas
