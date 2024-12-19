from fastapi import APIRouter, HTTPException
from app.schemas.quiz_response import QuizResponse
from app.services.quiz_service import generate_quiz

router = APIRouter()


@router.post("/", response_model=QuizResponse)
async def generate_quiz_endpoint(
    videoId: str, questions: int = 10, language: str = "pt-br"
):
    try:
        return generate_quiz(videoId, questions, language)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
