from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta

router = APIRouter()

SECRET_KEY = "secret123"


class User(BaseModel):
    username: str
    password: str


@router.post("/login")
def login(user: User):
    # dummy auth (replace with DB later)
    if user.username != "admin" or user.password != "admin":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = jwt.encode(
        {"sub": user.username, "exp": datetime.utcnow() + timedelta(hours=2)},
        SECRET_KEY,
        algorithm="HS256",
    )

    return {"access_token": token}
