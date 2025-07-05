from pydantic import BaseModel, Field
from typing import List, Union, Optional

class Question(BaseModel):
    questionType: str = Field(..., description="Type of question", enum=["MULTIPLE_CHOICE", "TRUE_OR_FALSE"])
    statement: str = Field(..., description="Question statement", examples=["What is the capital of France?", "Is the sky blue?"])
    hint: Optional[str] = Field(None, description="Hint for the question", examples=["It's a city known for the Eiffel Tower.", "Think about the color of the sky on a clear day."])
    explanation: Optional[str] = Field(None, description="Explanation of the answer", examples=["Paris is the capital of France.", "The sky appears blue due to Rayleigh scattering."])
    correctAnswer: str = Field(..., description="Correct answer", examples=["Option A", "True"])
    options: Optional[List[str]] = Field(None, description="Options for MULTIPLE_CHOICE", examples=["Option A", "Option B", "Option C", "Option D"])

