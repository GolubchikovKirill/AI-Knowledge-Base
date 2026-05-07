from fastapi import FastAPI
from app.db.database import engine
from app.db.models import Base, Document

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.document import DocumentCreate, DocumentResponse

app = FastAPI(
    title="AI Knowledge Base",
)
print(Base.metadata.tables)
Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/documents")
def create_document(
        document: DocumentCreate,
        db: Session = Depends(get_db),

):
    new_document = Document(filename=document.filename, filepath=document.filepath)

    db.add(new_document)
    db.commit()
    db.refresh(new_document)

    return new_document
