from typing import Any, Dict, Optional, Union

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.item import Item
from app.schemas.item import (ItemBase, ItemCreate, ItemCreateResponse,
                              ItemUpdate)


class CRUDItem(CRUDBase[ItemBase, ItemCreate, ItemUpdate]):

    def get_by_item_id(self, db: Session, *, item_id: str) -> Optional[Item]:
        return db.query(Item).filter(Item.item_id == item_id).first()

    def create(self, db: Session, *, obj_in: ItemCreate) -> ItemCreateResponse:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return ItemCreateResponse.from_orm(db_obj)

    def update(self, db: Session, *, db_obj: Item, obj_in: Union[ItemUpdate,
                                                                 Dict[str, Any]]) -> Item:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)


item = CRUDItem(Item)
