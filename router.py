from typing import Annotated

from fastapi import APIRouter, Depends

from schemas import STask, STaskAdd, STaskId
from repository import TaskRepository

router = APIRouter(prefix="/tasks", tags=["Задачи"])


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks


@router.post("")
async def create_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}
