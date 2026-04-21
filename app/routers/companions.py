from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter(prefix="/companions", tags=["Companions"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.Companion])
def get_companions(db: Session = Depends(get_db)):
    return crud.get_companions(db)