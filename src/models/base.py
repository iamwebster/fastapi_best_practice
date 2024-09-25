from src.models.db_helper import db_helper
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    
    id: Mapped[int] = mapped_column(primary_key=True)
