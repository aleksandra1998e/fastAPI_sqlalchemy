from pydantic import BaseModel


class RecipeBase(BaseModel):
    name: str
    time: int


class RecipeOut(RecipeBase):
    views: int
    id: int

    class Config:
        orm_mode = True


class RecipeById(RecipeBase):
    ingredients: str
    description: str

    class Config:
        orm_mode = True