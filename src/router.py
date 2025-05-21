from fastapi import APIRouter

from repository import TaskRepository
from schema import STaskAdd, STask, STaskID

router = APIRouter(prefix='/tasks')


@router.post('')
async def post_task(task: STaskAdd) -> STaskID:
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, 'task_id': task_id}


@router.get('')
async def get_task() -> list[STask]:
    tasks = await TaskRepository.get_all()
    return tasks
