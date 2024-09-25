from sqlalchemy import String 
from sqlalchemy.orm import Mapped, mapped_column

from src.models import Base 


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(255), unique=True)
    age: Mapped[int]
