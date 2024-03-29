from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    id: str
    category: Optional[str]
    quantity: int = 0


class ItemCreate(ItemBase):
    callname: Optional[str]
    description: Optional[str]
    price: Optional[int]
    image_url: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "id": "DD1391-100",
                "category": "Shoes",
                "quantity": 1,
                "callname": "덩크 로우 범고래",
                "description": "스테디셀러",
                "price": 119000,
                "image_url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fhypebeast.kr%2F2022%2F3%2Fnike-dunk-low-black-official-release-info&psig=AOvVaw1ac7rjz-I-UwN6H8pasuuE&ust=1686558150092000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCJCy8ezkuv8CFQAAAAAdAAAAABAE"
            }
        }


class ItemUpdate(BaseModel):
    id: str
    category: Optional[str]
    quantity: Optional[int]
    callname: Optional[str]
    description: Optional[str]
    price: Optional[int]
    image_url: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "id": "DD1391-100",
                "category": "Shoes",
                "quantity": 2,
                "callname": "덩크 로우 범고래",
                "description": "스테디셀러",
                "price": 119000,
                "image_url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fhypebeast.kr%2F2022%2F3%2Fnike-dunk-low-black-official-release-info&psig=AOvVaw1ac7rjz-I-UwN6H8pasuuE&ust=1686558150092000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCJCy8ezkuv8CFQAAAAAdAAAAABAE"
            }
        }


# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    callname: Optional[str]
    description: Optional[str]
    price: Optional[int]
    image_url: Optional[str]

    class Config:
        orm_mode = True


# Properties to return to client
class Item(ItemInDBBase):
    pass
