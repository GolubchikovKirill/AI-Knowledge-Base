from fastapi import FastAPI
from app.db.database import engine
from app.db.models import Base

app = FastAPI(
    title="AI Knowledge Base",
)
