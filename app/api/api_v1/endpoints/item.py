from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.item import ItemBase, ItemCreate, ItemCreateResponse

router = APIRouter()


@router.post("/create/", status_code=201, response_model=ItemCreateResponse)
def create_item(*, item_in: ItemCreate,
                db: Session = Depends(deps.get_db)) -> dict:
    """
    Create a new item in the database.
    """
    recipe = crud.item.create(db=db, obj_in=item_in)

    return recipe
