from pydantic import BaseModel
from typing import Optional

# base schema for create & apdate book
class BookBase(BaseModel):
    title: str
    author: str
    year: Optional[int] = None

# schema for create new book
class BookCreate(BookBase):
    pass

# schema for update book
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None

# schema for return book data
class BookOut(BookBase):
    id: int

    class Config:
        orm_mode = True
