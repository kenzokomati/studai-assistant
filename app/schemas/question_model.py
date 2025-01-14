from pydantic import BaseModel, Field
from typing import List, Union, Optional

class Question(BaseModel):
    questionType: str = Field(..., description="Type of question", enum=["MULTIPLE_CHOICE", "TRUE_OR_FALSE"])
    statement: str
    hint: Optional[str] = None
    explanation: Optional[str] = None
    correctAnswer: Union[str, int, List[str], bool] = Field(..., description="Correct answer")
    options: Optional[List[str]] = Field(None, description="Options for MULTIPLE_CHOICE")