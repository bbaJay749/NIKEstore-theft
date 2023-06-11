from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Item(Base):
    id = Column(String(length=256), primary_key=True)
    category = Column(String(length=256), nullable=False)
    callname = Column(String(length=256), nullable=True)
    quantity = Column(Integer, nullable=False)
    description = Column(String(length=256), nullable=True)
    price = Column(Integer, nullable=True)
    image_url = Column(String(length=1024), nullable=True)
