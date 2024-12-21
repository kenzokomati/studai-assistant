from app.services.transcript_service import get_transcript
from app.core.config import client
from app.schemas.quiz_response import QuizResponse

def generate_quiz(videoId: str, questionsNumber: int, language: str) -> QuizResponse:
    transcript = get_transcript(videoId)["transcript"]

    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"Create a quiz with {questionsNumber} questions based on the video transcript. The questions should be in {language}.",
            },
            {
                "role": "user",
                "content": transcript,
            },
        ],
        response_format=QuizResponse,
    )
    return response.choices[0].message.parsed
