from sqlalchemy import select

from database import TasksOrm, new_session
from schemas import STask, STaskAdd


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TasksOrm(**task_dict)

            session.add(task)
            await session.flush()
            await session.commit()

            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            result = await session.execute(select(TasksOrm))
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task) for task in task_models]
            return task_schemas
