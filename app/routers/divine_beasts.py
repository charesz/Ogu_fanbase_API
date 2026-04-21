from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter(prefix="/divine-beasts", tags=["Divine Beasts"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.DivineBeast])
def get_beasts(db: Session = Depends(get_db)):
    return crud.get_divine_beasts(db)


@router.get("/{beast_id}", response_model=schemas.DivineBeast)
def get_beast(beast_id: int, db: Session = Depends(get_db)):
    return crud.get_divine_beast(db, beast_id)