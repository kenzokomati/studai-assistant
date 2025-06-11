from pydantic import BaseModel
from enum import Enum

class SourceType(Enum):
    PROMPT_BASED = "PROMPT_BASED"
    YOUTUBE_VIDEO = "YOUTUBE_VIDEO"
    

class QuizRequest(BaseModel):
    sourceType: SourceType
    sourceContent: str
    questionsQuantity: int = 10
    languageCode: str = "PT" 