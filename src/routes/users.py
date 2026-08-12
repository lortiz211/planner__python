from fastapi import APIRouter, HTTPException, status

from src.models.users import User, UserSignIn

router = APIRouter(tags=["user"])

users: dict[str, User] = {}


@router.post("/signup")
async def sign_new_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied email exists",
        )

    users[data.email] = data
    return {"message": "User successfully registered"}


@router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if users[user.email] not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist",
        )

    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Username or password do not match",
        )

    return {"message": "User sign in successfully"}
