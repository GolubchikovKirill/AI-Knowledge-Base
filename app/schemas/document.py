from pydantic import BaseModel

class DocumentCreate(BaseModel):
    filename: str
    filepath: str

class DocumentResponse(BaseModel):
    id: int
    filename: str
    filepath: str

    model_config = {
        "from_attributes": True,
    }
