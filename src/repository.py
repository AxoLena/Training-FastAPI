from sqlalchemy import select

from schema import STaskAdd, STask
from database import new_session, TaskORM


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd):
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskORM(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskORM)
            result = await session.execute(query)
            tasks_models = result.scalars().all()
            task_schema = [STask.model_validate(task) for task in tasks_models]
            return task_schema
