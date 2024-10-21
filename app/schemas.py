from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str(min_length=1, max_lenght=200)

    class Config:
        orm_mode = True


class TaskUpdate(BaseModel):
    is_complete: bool

    class Config:
        orm_mode = True

class Task(BaseModel):
    id: int
    title: str
    is_complete: bool

    class Config:
        orm_mode = True
