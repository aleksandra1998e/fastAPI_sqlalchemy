from fastapi import FastAPI
from typing import List
from sqlalchemy.future import select
from models import Base, Recipe
from schemas import RecipeOut, RecipeById
from database import session, engine

app = FastAPI()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


@app.get("/recipes/", response_model=List[RecipeOut])
async def read_users():
    res = await session.execute(select(Recipe).order_by(Recipe.views.desc()).order_by(Recipe.time))
    return res.scalars().all()


@app.get("/recipes/{recipe_id}", response_model=RecipeById)
async def read_users(recipe_id: int):
    res = await session.execute(select(Recipe).filter(Recipe.id == recipe_id))
    return res.scalars().first()
