import sys, os
from src.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

class Candies(Base):
    __tablename__ = 'candies'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    state: Mapped[str] = mapped_column(String(30), nullable=False, server_default="full")
    owner: Mapped[str] = mapped_column(String(30), nullable=False, server_default="teacher")