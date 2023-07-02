from typing import Any, Dict, Optional, Union

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.item import Item
from app.schemas.item import (ItemBase, ItemCreate,
                              ItemUpdate)


class CRUDItem(CRUDBase[ItemBase, ItemCreate, ItemUpdate]):

    def temp(self, db: Session, *, db_obj: Item, obj_in: Union[ItemUpdate, Dict[str, Any]]) -> Item:
        # if isinstance(obj_in, dict):
        #     update_data = obj_in
        # else:
        #     update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=obj_in)


item = CRUDItem(Item)
