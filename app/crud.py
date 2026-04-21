from sqlalchemy.orm import Session
from . import models


# --------------------
# CHARACTERS
# --------------------
def get_characters(db: Session):
    return db.query(models.Character).all()


def get_character(db: Session, character_id: int):
    return db.query(models.Character).filter(
        models.Character.id == character_id
    ).first()


# --------------------
# DIVINE BEASTS 
# --------------------
def get_divine_beasts(db: Session):
    return db.query(models.DivineBeast).all()


def get_divine_beast(db: Session, beast_id: int):
    return db.query(models.DivineBeast).filter(
        models.DivineBeast.id == beast_id
    ).first()


# --------------------
# COMPANIONS
# --------------------
def get_companions(db: Session):
    return db.query(models.Companion).all()


# --------------------
# NPCS
# --------------------
def get_npcs(db: Session):
    return db.query(models.NPC).all()


# --------------------
# ITEMS
# --------------------
def get_items(db: Session):
    return db.query(models.Item).all()


# --------------------
# COLLECTIBLES
# --------------------
def get_collectibles(db: Session, type: str = None, region: str = None):
    query = db.query(models.Collectible)

    if type:
        query = query.filter(models.Collectible.type == type)

    if region:
        query = query.filter(models.Collectible.region == region)

    return query.all()