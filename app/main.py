from fastapi import FastAPI
from app.routers.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(auth_router)

@app.get("/")
def health_check():
    return {"message": "API is working"}
