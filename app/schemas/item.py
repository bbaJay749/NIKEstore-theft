from typing import Optional

from pydantic import BaseModel
from sqlalchemy import BLOB


class ItemBase(BaseModel):
    item_id: Optional[str]
    category: Optional[str]
    quantity: int = 0


class ItemCreate(ItemBase):
    callname: Optional[str]
    description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "item_id": "DD1391-100",
                "category": "Shoes",
                "quantity": 1,
                "callname": "덩크 로우 범고래",
                "description": "스테디셀러"
            }
        }


class ItemCreateResponse(ItemCreate):
    class Config:
        orm_mode = True,


class ItemUpdate(ItemBase):
    quantity: int
    callname: Optional[str]
    description: Optional[str]
    image = BLOB
