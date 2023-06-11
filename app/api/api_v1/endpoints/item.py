from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.item import ItemCreate, ItemInDBBase

router = APIRouter()


@router.get("/{item_id}", status_code=200, response_model=ItemInDBBase)
def fetch_item(*, item_id: str, db: Session = Depends(deps.get_db)) -> ItemInDBBase:
    """
    Get an item in the database. search by item_id.
    """
    result = crud.item.get(db=db, id=item_id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Item with ID {item_id} not exists"
        )

    return ItemInDBBase.from_orm(result)


@router.post("/create", status_code=201, response_model=ItemInDBBase)
def create_item(*, item_in: ItemCreate,
                db: Session = Depends(deps.get_db)) -> ItemInDBBase:
    """
    Create a new item in the database.
    """
    if crud.item.get(db, item_in.id):
        raise HTTPException(
            status_code=404, detail=f"Item with ID {item_in.id} already exists"
        )

    result = crud.item.create(db=db, obj_in=item_in)

    return ItemInDBBase.from_orm(result)


@router.delete("/delete/{item_id}", status_code=200, response_model=ItemInDBBase)
def delete_item(*, item_id: str, db: Session = Depends(deps.get_db)) -> ItemInDBBase:
    """
    Delete an item in the database. search by item_id.
    """
    if not crud.item.get(db, item_id):
        raise HTTPException(status_code=404, detail=f"Item not found with item_id {item_id}")

    result = crud.item.remove(db=db, id=item_id)

    return ItemInDBBase.from_orm(result)
