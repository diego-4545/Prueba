from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
import models, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items")
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    nuevo = models.Item(nombre=item.nombre)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@app.get("/items")
def get_items(db: Session = Depends(get_db)):
    return db.query(models.Item).all()
