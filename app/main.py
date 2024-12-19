from fastapi import FastAPI
from app.api import quiz, transcript

app = FastAPI()

# Include API routers
app.include_router(quiz.router, prefix="/api/quiz", tags=["Quiz"])
app.include_router(transcript.router, prefix="/api/transcript", tags=["Transcript"])
