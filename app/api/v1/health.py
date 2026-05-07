from app.main import app

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
