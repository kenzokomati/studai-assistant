from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from youtube_transcript_api import YouTubeTranscriptApi
from typing import List, Union, Optional
from openai import OpenAI

import os

import QuizResponseConfig

app = FastAPI()

client = OpenAI(
    organization=os.environ.get("OPENAI_ORGANIZATION_ID"),
    project=os.environ.get("OPENAI_PROJECT_ID"),
)

#   enum = "SHORT_ANSWER", "FILL_THE_BLANK",
#   descrition = String for SHORT_ANSWER, Array for FILL_THE_BLANK,
class Question(BaseModel):
    questionType: str = Field(
        ...,
        description="Type of question",
        enum=["MULTIPLE_CHOICE", "TRUE_OR_FALSE"],
    )
    statement: str
    hint: Optional[str] = None
    explanation: Optional[str] = None
    correctAnswer: Union[str, int, List[str], bool] = Field(
        ...,
        description=" Integer for MULTIPLE_CHOICE, Boolean for TRUE_OR_FALSE",
    )
    options: Optional[List[str]] = Field(
        None, description="Only used for MULTIPLE_CHOICE questions"
    )


class QuizResponse(BaseModel):
    title: str
    description: str
    questions: List[Question]
    QuizResponseConfig


# Content = In the FILL_THE_BLANK questions, use '___BLANK___' as the placeholder.
@app.post("/api/quiz")
async def generateQuiz(videoId: str, questions: int = 10):
    transcript = loadVideoTranscript(videoId)["transcript"]

    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"You are a teacher and you need to create a quiz for your students based on the video transcript. The quiz should have {questions} questions.",
            },
            {
                "role": "user",
                "content": f"Create a quiz for this video transcript: {transcript}",
            },
        ],
        response_format=QuizResponse,
    )

    return response.choices[0].message.parsed


@app.get("/api/transcript")
async def getVideoTranscript(videoId: str, timestampEnabled: bool = False):
    try:
        return loadVideoTranscript(videoId, timestampEnabled)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def loadVideoTranscript(videoId: str, timestampEnabled: bool = False):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(
            videoId, languages=["en", "pt"]
        )
        if not timestampEnabled:
            transcript = " ".join(line["text"] for line in transcript).strip()
        return {"transcript": transcript}
    except Exception as e:
        raise HTTPException(
            status_code=404, detail="Transcript not found or unavailable."
        )
