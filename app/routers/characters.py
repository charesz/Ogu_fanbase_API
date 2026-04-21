from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter(prefix="/characters", tags=["Characters"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.Character])
def get_characters(db: Session = Depends(get_db)):
    return crud.get_characters(db)


@router.get("/{character_id}", response_model=schemas.Character)
def get_character(character_id: int, db: Session = Depends(get_db)):
    return crud.get_character(db, character_id)