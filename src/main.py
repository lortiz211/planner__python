from fastapi import FastAPI

from src.routes.events import router as events_router
from src.routes.users import router as user_router

app = FastAPI()

# Register routes here
app.include_router(user_router)
app.include_router(events_router)
