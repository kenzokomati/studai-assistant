from fastapi import FastAPI
from app.api import quiz, transcript
from app.middleware.logging_middleware import LoggingMiddleware

app = FastAPI()

# Custom logging middleware
app.add_middleware(LoggingMiddleware)

# Include API routers
app.include_router(quiz.router, prefix="/api/quiz", tags=["Quiz"])
app.include_router(transcript.router, prefix="/api/transcript", tags=["Transcript"])

@app.get("/")  # Health check endpoint
def read_root():
    return {"message": "Hello, World!"}  # Should return 200 OK

@app.get("/health")
def health_check():
    return {"status": "ok"}