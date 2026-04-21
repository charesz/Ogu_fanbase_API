from fastapi import FastAPI
from .database import engine
from . import models, seed

from .routers import (
    characters,
    divine_beasts,
    companions,
    npcs,
    items,
    collectibles
)

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ogu Fanbase API")

# include routers
app.include_router(characters.router)
app.include_router(divine_beasts.router)
app.include_router(companions.router)
app.include_router(npcs.router)
app.include_router(items.router)
app.include_router(collectibles.router)


@app.get("/")
def root():
    return {"message": "Ogu Fanbase API is running"}


@app.on_event("startup")
def startup():
    seed.seed_data()