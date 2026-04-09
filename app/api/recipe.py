from fastapi import APIRouter
from app.service.invoke import invoke_model

router = APIRouter()

@router.post("/recipes/")
def get_recipes(query: str | None = "I have chicken, give some main dish for lunch"):
    return invoke_model(query)







