from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database.connection import conn
from src.routes.events import router as events_router
from src.routes.users import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    conn()
    yield


app = FastAPI(lifespan=lifespan)

# Register routes here
app.include_router(user_router)
app.include_router(events_router)
