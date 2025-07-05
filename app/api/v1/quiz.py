from fastapi import APIRouter, HTTPException
from app.schemas.quiz import Quiz
from app.services.quiz_service import generate_quiz
from app.schemas.quiz_request import QuizRequest

router = APIRouter()

@router.post("/", response_model=Quiz)
async def generate_quiz_endpoint(request: QuizRequest):
    try:
        return generate_quiz(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 