from fastapi import APIRouter, status
from app.schemas.users import RegisterRequest
from app.core.security import hash_password

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(payload: RegisterRequest):
    password_hash = hash_password(payload.password)

    return {
        "message": "User registered successfully",
        "email": payload.email,
        "full_name": payload.full_name,
        "password_hash": password_hash  # şimdilik gösteriyoruz (debug)
    }

@router.post("/login", status_code=status.HTTP_200_OK)
def login():
    return {"message": "User login successfully"}
