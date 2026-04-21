from pydantic import BaseModel


class Character(BaseModel):
    id: int
    name: str
    description: str
    role: str
    is_playable: bool

    class Config:
        from_attributes = True

class DivineBeast(BaseModel):
    id: int
    name: str
    title: str
    domain: str
    description: str
    element: str
    legacy: str
    attribute: str

    class Config:
        from_attributes = True


class Companion(BaseModel):
    id: int
    name: str
    region: str
    ability: str
    description: str
    type: str

    class Config:
        from_attributes = True


class NPC(BaseModel):
    id: int
    name: str
    region: str
    description: str
    chat: str

    class Config:
        from_attributes = True


class Item(BaseModel):
    id: int
    name: str
    effect: str
    region: str

    class Config:
        from_attributes = True


class Collectible(BaseModel):
    id: int
    name: str
    type: str
    region: str
    location: str
    rarity: str | None

    class Config:
        from_attributes = True