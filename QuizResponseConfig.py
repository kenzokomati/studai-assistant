class Config:
    schema_extra = {
        "example": {
            "title": "Sample Quiz",
            "description": "A quiz based on a video transcript",
            "questions": [
                {
                    "questionType": "MULTIPLE_CHOICE",
                    "statement": "What is the capital of France?",
                    "hint": "It's also known as the city of light",
                    "explanation": "Paris is the capital and largest city of France.",
                    "correctAnswer": 1,
                    "options": ["Berlin", "Paris", "Rome", "Madrid"],
                },
                {
                    "questionType": "SHORT_ANSWER",
                    "statement": "Name the process by which plants make their food.",
                    "hint": "It starts with 'photo-'",
                    "explanation": "Photosynthesis is the process by which plants make their food using sunlight.",
                    "correctAnswer": "Photosynthesis",
                },
                {
                    "questionType": "FILL_THE_BLANK",
                    "statement": "Water boils at ___BLANK___ degrees Celsius.",
                    "hint": "It is a round number",
                    "explanation": "Water boils at 100 degrees Celsius.",
                    "correctAnswer": ["100"],
                },
                {
                    "questionType": "TRUE_OR_FALSE",
                    "statement": "The sun rises in the west.",
                    "hint": "Think about where the sun rises",
                    "explanation": "The sun rises in the east.",
                    "correctAnswer": False,
                },
            ],
        }
    }
