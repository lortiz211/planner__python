from fastapi import APIRouter, Body, HTTPException, status

from src.models.events import Event

router = APIRouter(tags=["Events"], prefix="/events")

events: list[Event] = []


@router.get("/", response_model=list[Event])
async def retrieve_all_events() -> list[Event]:
    return events


@router.get("/{id}", response_model=Event)
async def retrieve_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with provided Id does not exists",
    )


@router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:  # noqa: B008
    events.append(body)
    return {"message": "Event created successfully"}


@router.delete("/{id}")
async def delte_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {"message": "Event deleted successfully"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with provided Id does not exists",
    )


@router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {"message": "All events deleted successfully"}
