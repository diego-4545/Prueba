from pydantic import BaseModel

class ItemCreate(BaseModel):
    nombre: str

class ItemResponse(ItemCreate):
    id: int

    class Config:
        orm_mode = True
