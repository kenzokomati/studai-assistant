from fastapi import FastAPI
from app.api import quiz, transcript

app = FastAPI()

# Include API routers
app.include_router(quiz.router, prefix="/api/quiz", tags=["Quiz"])
app.include_router(transcript.router, prefix="/api/transcript", tags=["Transcript"])

@app.get("/")  # Health check endpoint
def read_root():
    return {"message": "Hello, World!"}  # Should return 200 OK

@app.get("/health")
def health_check():
    return {"status": "ok"}