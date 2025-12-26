from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import Column, Integer, String
from app.db.database import Base

#-------------------------
#   Register Schemas
#-------------------------

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    full_name: str

class RegisterResponse(BaseModel):
    message: str
    email: EmailStr
    full_name: str

#-------------------------
#   Login Schemas
#-------------------------    

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

#-------------------------
#   User Schema
#-------------------------    

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)