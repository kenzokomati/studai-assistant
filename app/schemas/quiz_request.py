from pydantic import BaseModel
from enum import Enum

class SourceType(Enum):
    PROMPT_BASED = "PROMPT_BASED"
    YOUTUBE_VIDEO = "YOUTUBE_VIDEO"

class LanguageCode(Enum):
    EN = "EN"
    PT = "PT"

class QuizRequest(BaseModel):
    sourceType: SourceType
    sourceContent: str
    questionsQuantity: int = 10
    languageCode: LanguageCode = LanguageCode.EN