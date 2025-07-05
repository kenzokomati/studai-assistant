from pydantic import BaseModel, Field
from typing import List
from app.schemas.question import Question

class Quiz(BaseModel):
    title: str = Field(..., description="Title of the quiz", examples=["Math for Beginners", "History of Ancient Rome"])
    description: str = Field(..., description="Description of the quiz", examples=["A beginner-friendly quiz on basic math concepts.", "Test your knowledge on the history of Ancient Rome."])
    questions: List[Question] = Field(..., description="List of questions in the quiz")
