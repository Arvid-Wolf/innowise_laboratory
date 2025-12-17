from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# create books.db
DATABASE_URL = "sqlite:///./books.db"

# engine for connection to db
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# sessions creator for db 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class for ORM models
Base = declarative_base()
