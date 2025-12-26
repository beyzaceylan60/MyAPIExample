from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Auth Example")

app.include_router(auth_router)

@app.get("/")
def health_check():
    return {"message": "API is working"}
