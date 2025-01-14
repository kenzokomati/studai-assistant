from pydantic import BaseModel, Field
from typing import List
from app.schemas.question_model import Question

class Quiz(BaseModel):
    title: str
    description: str
    questions: List[Question]
