from fastapi import FastAPI
from app.api.v1 import transcript
from app.api.v1 import quiz
from app.middleware.logging import LoggingMiddleware

app = FastAPI()

# Custom logging middleware
app.add_middleware(LoggingMiddleware)

# Include API routers
app.include_router(quiz.router, prefix="/api/v1/quizzes", tags=["Quizzes"])
app.include_router(transcript.router, prefix="/api/v1/transcripts", tags=["Transcripts"])

@app.get("/")  # Health check endpoint
def read_root():
    return {"message": "Hello, World!"}  # Should return 200 OK

@app.get("/health")
def health_check():
    return {"status": "ok"}