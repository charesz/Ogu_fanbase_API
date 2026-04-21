from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter(prefix="/collectibles", tags=["Collectibles"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.Collectible])
def get_collectibles(
    type: str | None = None,
    region: str | None = None,
    db: Session = Depends(get_db)
):
    return crud.get_collectibles(db, type=type, region=region)