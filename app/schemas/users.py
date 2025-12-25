from pydantic import BaseModel, EmailStr, Field

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
    message: str

