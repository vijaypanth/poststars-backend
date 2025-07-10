from fastapi import FastAPI
from app.routers import campaigns,users
from app import models
from app.database import engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Poststars Backend")

app.include_router(campaigns.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Poststars Backend Running"}

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","https://poststars-frontend.vercel.app",],  # adjust if deploying
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)