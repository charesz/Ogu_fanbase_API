from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    role = Column(String)
    is_playable = Column(Boolean, default=False)

class DivineBeast(Base):
    __tablename__ = "divine_beasts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    title = Column(String)         
    domain = Column(String)         
    description = Column(String)
    element = Column(String)        
    legacy = Column(String)         
    attribute = Column(String)      

class Companion(Base):
    __tablename__ = "companions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    region = Column(String)
    ability = Column(String)
    description = Column(String)
    type = Column(String)


class NPC(Base):
    __tablename__ = "npcs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    region = Column(String)
    description = Column(String)
    chat = Column(String)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    effect = Column(String)
    region = Column(String)


class Collectible(Base):
    __tablename__ = "collectibles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    region = Column(String)
    location = Column(String)
    rarity = Column(String, nullable=True)