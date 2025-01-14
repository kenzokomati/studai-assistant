from fastapi import APIRouter, HTTPException
from app.schemas.quiz_model import Quiz
from app.services.quiz_service import generate_quiz

router = APIRouter()

@router.post("/", response_model=Quiz)
async def generate_quiz_endpoint(
    videoId: str, questionsNumber: int = 10, language: str = "pt-br"
):
    try:
        return generate_quiz(videoId, questionsNumber, language)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 