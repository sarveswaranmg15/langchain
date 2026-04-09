from fastapi import FastAPI
from app.api.recipe import router as recipe_router

app = FastAPI(title="Recommend a Recipe")

@app.get("/")
def say_():
    return "HI, Welcomeee!!!"

app.include_router(recipe_router,prefix="/langchain",tags=["Recipes"])