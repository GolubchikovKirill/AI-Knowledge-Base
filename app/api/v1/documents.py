from app.db.models import Document
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.schemas.document import DocumentCreate, DocumentResponse
from app.main import app

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

@app.get("/getDocuments", response_model=list[DocumentResponse])
def get_documents(db: Session = Depends(get_db)) -> list[type[Document]]:
    documents = db.query(Document).all()
    return documents
