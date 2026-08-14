from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlmodel import Session, select

from src.database.connection import get_session
from src.models.events import Event, EventUpdate

router = APIRouter(tags=["Events"], prefix="/events")

events: list[Event] = []


@router.get("/", response_model=list[Event])
async def retrieve_all_events(session: Session = Depends(get_session)) -> list[Event]:  # noqa: B008
    statement = select(Event)
    events = session.exec(statement).all()
    return events  # ty: ignore[invalid-return-type]


@router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session=Depends(get_session)) -> Event:  # noqa: B008
    event = session.get(Event, id)
    if event:
        return event

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with provided Id does not exists",
    )


@router.post("/")
async def create_event(
    new_event: Event = Body(...),  # noqa: B008
    session: Session = Depends(get_session),  # noqa: B008
) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    return {"message": "Event created successfully"}


@router.put("/{id}", response_model=Event)
async def update_event(
    id: int,
    new_data: EventUpdate,
    session: Session = Depends(get_session),  # noqa: B008
) -> Event:
    event = session.get(Event, id)
    if event is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with provided Id does not exists",
        )

    event_data = new_data.model_dump(exclude_unset=True)
    for key, value in event_data.items():
        setattr(event, key, value)

    session.add(event)
    session.commit()
    session.refresh(event)

    return event


@router.delete("/{id}")
async def delte_event(
    id: int,
    session: Session = Depends(get_session),  # noqa: B008
) -> dict:
    event = session.get(Event, id)

    if event:
        session.delete(event)
        session.commit()
        return {"message": "Event deleted successfully"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with provided Id does not exists",
    )


@router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {"message": "All events deleted successfully"}
