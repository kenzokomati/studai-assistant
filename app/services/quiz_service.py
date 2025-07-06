from fastapi import UploadFile
from app.schemas.quiz import Quiz
from app.schemas.message import Message
from app.schemas.quiz_request import LanguageCode, QuizRequest
from app.schemas.quiz_request import SourceType

from app.services.file_service import extract_pdf_content
from app.utils.prompts import read_prompts_file
from app.services.transcript_service import get_transcript
from app.clients.openai_client import requestChatCompletion

QUIZ_GENERATION_INSTRUCTIONS = read_prompts_file("quiz_generation_instructions")

def generate_quiz(request: QuizRequest) -> Quiz:

    instructions_message = Message(
        role="system",
        content=QUIZ_GENERATION_INSTRUCTIONS
    )

    system_message = assemble_system_message(request)
    user_message = assemble_user_message(request)

    return requestChatCompletion(
        messages=[
            instructions_message,
            system_message,
            user_message
        ],
        response_format=Quiz
    )

def generate_quiz_from_file(file: UploadFile, sourceType: SourceType,
    questionsQuantity: int, languageCode: LanguageCode,
    startPage: int, endPage: int) -> Quiz:

    parsed_request = QuizRequest(
        sourceType=sourceType,
        sourceContent=extract_pdf_content(file, startPage, endPage),
        questionsQuantity=questionsQuantity,
        languageCode=languageCode
    )

    instructions_message = Message(
        role="system",
        content=QUIZ_GENERATION_INSTRUCTIONS
    )

    system_message = assemble_system_message(parsed_request)
    user_message = assemble_user_message(parsed_request)

    return requestChatCompletion(
        messages=[
            instructions_message,
            system_message,
            user_message
        ],
        response_format=Quiz
    )


    
def assemble_system_message(request: QuizRequest) -> Message:
    content = None
    if request.sourceType == SourceType.PROMPT_BASED:
        content = f"""You are a quiz generator. Create a quiz with {request.questionsQuantity} questions and answers in {request.languageCode} language. All parts of the quiz — including title, description, question statements, options, hints, explanations, and answers — must be written entirely in the language identified by the language code: "{request.languageCode}"."""
        
    elif request.sourceType == SourceType.YOUTUBE_VIDEO:
        content = f"""You are a quiz generator. Based on the following video transcript, generate a quiz with {request.questionsQuantity} questions in {request.languageCode}. The transcript may include informal speech, digressions, and filler words — ignore those and focus on extracting the key ideas."""

    elif request.sourceType == SourceType.PDF_CONTENT:
        content = f"""You are a quiz generator. Based on the following PDF content, generate a quiz with {request.questionsQuantity} questions in {request.languageCode}. The content may include informal speech, digressions, and filler words — ignore those and focus on extracting the key ideas."""
        
    else:
        raise ValueError(f"Invalid sourceType: {request.sourceType}.")
    
    return Message(
        role="system",
        content=content
    )

def assemble_user_message (request: QuizRequest) -> Message:
    content = None
    if request.sourceType == SourceType.PROMPT_BASED:
        content = f'Generate a quiz with {request.questionsQuantity} questions in {request.languageCode} language. The quiz should cover the following topic: "{request.sourceContent}".'
    
    elif request.sourceType == SourceType.YOUTUBE_VIDEO:
        transcript = get_transcript(request.sourceContent)

        if not transcript or not transcript.get("transcript"):
            raise ValueError("Transcript not found or unavailable.")
        
        content = f'Generate a quiz with {request.questionsQuantity} questions in {request.languageCode} language based on the following transcript: "{transcript}".'

    elif request.sourceType == SourceType.PDF_CONTENT:
        content = f'Generate a quiz with {request.questionsQuantity} questions in {request.languageCode} language based on the following PDF content: "{request.sourceContent}".'
    
    else:
        raise ValueError(f"Invalid sourceType: {request.sourceType}.")

    return Message(
        role="user",
        content=content
    )
