from pydantic import BaseModel, ConfigDict

class ItemCreate(BaseModel):
    nombre: str

class ItemResponse(ItemCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
