from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Database cleaned up")
    await create_tables()
    print("Database created")
    yield
    print("Database closed")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
