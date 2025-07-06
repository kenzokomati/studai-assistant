from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from app.schemas.quiz import Quiz
from app.services.quiz_service import generate_quiz, generate_quiz_from_file
from app.schemas.quiz_request import LanguageCode, QuizRequest, SourceType

router = APIRouter()

@router.post("/", response_model=Quiz)
async def generate_quiz_endpoint(request: QuizRequest):
    try:
        return generate_quiz(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/from-file", response_model=Quiz)
async def generate_quiz_from_file_endpoint(
    file: UploadFile = File(...),
    sourceType: SourceType = Form(...),
    questionsQuantity: int = Form(10),
    languageCode: LanguageCode = Form(LanguageCode.EN),
    startPage: int = Form(1),
    endPage: int = Form(25)
):
    try:
        return generate_quiz_from_file(
            file=file,
            sourceType=sourceType,
            questionsQuantity=questionsQuantity,
            languageCode=languageCode,
            startPage=startPage,
            endPage=endPage
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 