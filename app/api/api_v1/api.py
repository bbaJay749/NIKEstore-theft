from fastapi import APIRouter

from app.api.api_v1.endpoints import item, recipe


api_router = APIRouter()
api_router.include_router(recipe.router, prefix="/recipes", tags=["recipes"])
api_router.include_router(item.router, prefix="/items", tags=["items"])
