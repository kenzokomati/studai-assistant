from app.services.transcript_service import get_transcript
from app.core.config import client
from app.schemas.quiz_response import QuizResponse
from app.schemas.quiz_request import QuizRequest
from app.schemas.quiz_request import SourceType

instructions_to_format_response = ("""
    IMPORTANT: Respect the specified language strictly. Do not mix languages. Translate any internal labels like "True" / "False" or "Correct" / "Incorrect" into the target language.
    - Each question must include the following fields:\n
      - 'questionType': 'MULTIPLE_CHOICE' or 'TRUE_OR_FALSE'.\n
      - 'statement': The question itself.\n
      - 'hint': A short hint to help the user.\n
      - 'explanation': A brief explanation for the correct answer.\n
      - 'correctAnswer': A string with correct option.\n
      - 'options': A list of 4 options for multiple choice questions or true/false (respect the language preference).\n\n
    Also include:\n
    - A 'title' summarizing the theme of the quiz.\n
    - A 'description' of what the quiz covers.\n\n
    Output must strictly follow the QuizResponse format.
""")

def generate_quiz(request: QuizRequest) -> QuizResponse:
    if request.sourceType == SourceType.YOUTUBE_VIDEO: 
        return generate_video_quiz(request)
    elif request.sourceType == SourceType.PROMPT_BASED:
        return generate_prompt_quiz(request)
    else:
        raise ValueError(f"Invalid typeQuiz. Must be '{SourceType.YOUTUBE_VIDEO}' or '{SourceType.PROMPT_BASED}'.")
    
def generate_prompt_quiz(request: QuizRequest) -> QuizResponse:
    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                            f"""You are a quiz generator. Create a quiz with {request.questionsQuantity} questions and answers in {request.languageCode} language.
                            All parts of the quiz — including title, description, question statements, options, hints, explanations, and answers — must be written entirely in the language identified by the language code: "{request.languageCode}".
                            based on the content provided by the user. The quiz must follow this structure:\n\n 
                            {instructions_to_format_response}"""
                        )
            },
            {
                "role": "user",
                "content": request.sourceContent,
            },
        ],
        response_format=QuizResponse,
    )
    return response.choices[0].message.parsed

def generate_video_quiz(request: QuizRequest) -> QuizResponse:
    transcript = get_transcript(request.sourceContent)["transcript"]

    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                            f"""You are a quiz generator. Based on the following video transcript, generate a quiz with {request.questionsQuantity} questions in {request.languageCode}.\n\n
                            The transcript may include informal speech, digressions, and filler words — ignore those and focus on extracting the key ideas.\n\n
                            {instructions_to_format_response}"""
                        )
            },
            {
                "role": "user",
                "content": transcript,
            },
        ],
        response_format=QuizResponse,
    )
    return response.choices[0].message.parsed
