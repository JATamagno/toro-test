from pydantic import BaseModel, EmailStr, ConfigDict

class Message(BaseModel):
    message: str

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)

class UserDB(UserSchema):
    id: int

class UserList(BaseModel):
    users: list[UserPublic]

class LoginRequest(BaseModel):
    email: str
    password: str
