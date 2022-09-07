from sqlalchemy import Column, Integer, String

from database import Base


class Recipe(Base):
    __tablename__ = "recipe"

    id = Column(Integer, primary_key=True, index=True)
    views = Column(Integer, index=True)
    name = Column(String, index=True)
    time = Column(Integer, index=True)
    ingredients = Column(String, index=True)
    description = Column(String, index=True)
