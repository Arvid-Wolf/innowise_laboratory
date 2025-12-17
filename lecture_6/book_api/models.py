from sqlalchemy import Column, Integer, String
from database import Base

# define book table
class Book(Base):
    __tablename__ = "books"

    # database table fields
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=True)
